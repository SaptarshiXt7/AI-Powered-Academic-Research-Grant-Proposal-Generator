import streamlit as st
import sys
import io
import threading
import time
from crew import crew

st.set_page_config(page_title="AI Research Assistant", page_icon="🔬", layout="wide")

st.title("🔬 AI-Powered Academic Research Assistant")

topic = st.text_input("Enter Research Topic", placeholder="e.g. AI in Healthcare, Quantum Computing...")

if st.button("🚀 Generate", type="primary"):
    if not topic.strip():
        st.warning("Please enter a research topic first!")
    else:
        # Container for live output
        status_container = st.status("🧠 AI Agents are working...", expanded=True)
        live_output = status_container.empty()

        # Capture CrewAI verbose output in real-time
        captured_output = io.StringIO()
        original_stdout = sys.stdout
        result_holder = {"result": None, "error": None}

        class StreamCapture(io.TextIOBase):
            """Captures stdout and writes to StringIO buffer."""
            def __init__(self, buffer):
                self.buffer = buffer
                self.original = original_stdout

            def write(self, s):
                if s and s.strip():
                    self.buffer.write(s)
                # Also write to original stdout for terminal
                try:
                    self.original.write(s)
                except:
                    pass
                return len(s) if s else 0

            def flush(self):
                try:
                    self.original.flush()
                except:
                    pass

        def run_crew():
            try:
                sys.stdout = StreamCapture(captured_output)
                result_holder["result"] = crew.kickoff(inputs={"topic": topic})
            except Exception as e:
                result_holder["error"] = str(e)
            finally:
                sys.stdout = original_stdout

        # Run crew in background thread
        thread = threading.Thread(target=run_crew)
        thread.start()

        # Show live progress while crew runs
        dots = ""
        while thread.is_alive():
            current_output = captured_output.getvalue()
            if current_output.strip():
                # Show the latest captured verbose output
                lines = current_output.strip().split("\n")
                # Show last 30 lines to keep it readable
                display_lines = lines[-30:]
                live_output.code("\n".join(display_lines), language=None)
            else:
                dots = dots + "." if len(dots) < 3 else ""
                live_output.markdown(f"⏳ Waiting for AI agents to start{dots}")
            time.sleep(0.5)

        thread.join()

        # Show final status
        if result_holder["error"]:
            status_container.update(label="❌ Error occurred", state="error")
            st.error(result_holder["error"])
        else:
            status_container.update(label="✅ Research Complete!", state="complete")

            # Display final result beautifully
            st.divider()
            st.subheader("📄 Research Output")

            result = result_holder["result"]
            # CrewAI result can be a CrewOutput object
            result_text = str(result.raw) if hasattr(result, 'raw') else str(result)

            st.markdown(result_text)