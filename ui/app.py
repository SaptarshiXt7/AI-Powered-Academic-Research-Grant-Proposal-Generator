import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
from main import run_pipeline

st.title("AI Academic Research Assistant")

topic = st.text_input("Enter Research Topic")

if st.button("Generate Research Analysis"):
    with st.spinner("Running AI agents..."):
        result = run_pipeline(topic)

    st.subheader("Generated Output")
    st.markdown(result)