import sys  
import os  
sys.path.append(os.path.dirname(os.path.dirname(__file__)))   #path to the main.py file

import streamlit as st  #to import the streamlit library
from main import run_pipeline  #to import the run_pipeline function from the main.py file

st.title("AI Academic Research Assistant")  #title of the app

topic = st.text_input("Enter Research Topic")  #text input for the research topic

if st.button("Generate Research Analysis"):  #button to generate the research analysis
    with st.spinner("Running AI agents..."):  #spinner to show that the AI agents are running
        result = run_pipeline(topic)  #running the run_pipeline function with the research topic

    st.subheader("Generated Output")  #subheader for the generated output
    st.markdown(result)  #markdown for the generated output (Plain text --> it will generate it with special symbols)