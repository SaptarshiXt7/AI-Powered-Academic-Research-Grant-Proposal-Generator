# \# AI-Powered Academic Research Assistant \& Grant Proposal Generator

# 

# \## Overview

# 

# This project is an \*\*AI-powered academic research assistant\*\* that helps users analyze a research topic and automatically generate:

# 

# \* Research keywords

# \* Literature review summary

# \* Research gaps

# \* Research grant proposal

# 

# The system uses \*\*CrewAI multi-agent architecture\*\* where multiple AI agents collaborate to complete different research tasks.

# 

# The application includes a \*\*Streamlit web interface\*\* where users can input a research topic and generate results.

# 

# \---

# 

# \# System Architecture

# 

# The system uses \*\*multi-agent collaboration\*\*:

# 

# 1\. \*\*Research Planner Agent\*\*

# 

# &#x20;  \* Analyzes the research topic

# &#x20;  \* Generates research keywords

# 

# 2\. \*\*Literature Review Agent\*\*

# 

# &#x20;  \* Summarizes academic literature

# &#x20;  \* Synthesizes research findings

# 

# 3\. \*\*Research Gap Analyst Agent\*\*

# 

# &#x20;  \* Identifies missing areas in current research

# 

# 4\. \*\*Grant Proposal Writer Agent\*\*

# 

# &#x20;  \* Generates a structured research proposal

# 

# The system also uses \*\*RAG (Retrieval-Augmented Generation)\*\* with vector embeddings to retrieve relevant research content.

# 

# \---

# 

# \# Tech Stack

# 

# \* Python

# \* CrewAI (multi-agent orchestration)

# \* Ollama (local LLM)

# \* Llama3 / Phi3 models

# \* FAISS (vector database)

# \* HuggingFace Embeddings

# \* Streamlit (UI)

# \* LangChain ecosystem

# 

# \---

# 

# \# Requirements

# 

# \* Python \*\*3.10 or higher\*\*

# \* Ollama installed

# \* Git installed

# 

# \---

# 

# \# Step 1: Clone the Repository

# 

# ```bash

# git clone https://github.com/YOUR\_USERNAME/research-assistant.git

# cd research-assistant

# ```

# 

# \---

# 

# \# Step 2: Create Virtual Environment

# 

# Windows:

# 

# ```bash

# python -m venv venv

# venv\\Scripts\\activate

# ```

# 

# Mac/Linux:

# 

# ```bash

# python3 -m venv venv

# source venv/bin/activate

# ```

# 

# \---

# 

# \# Step 3: Install Dependencies

# 

# ```bash

# pip install -r requirements.txt

# ```

# 

# \---

# 

# \# Step 4: Install and Run Ollama

# 

# Download Ollama:

# 

# https://ollama.com/download

# 

# Start Ollama:

# 

# ```bash

# ollama serve

# ```

# 

# \---

# 

# \# Step 5: Download the LLM Model

# 

# Example using \*\*Llama3\*\*

# 

# ```bash

# ollama pull llama3

# ```

# 

# Verify installation:

# 

# ```bash

# ollama list

# ```

# 

# \---

# 

# \# Step 6: Run the Application

# 

# Start the Streamlit interface:

# 

# ```bash

# streamlit run ui/app.py

# ```

# 

# The app will open automatically in your browser.

# 

# If it does not open, visit:

# 

# ```

# http://localhost:8501

# ```

# 

# \---

# 

# \# Step 7: Use the Application

# 

# 1\. Enter a \*\*research topic\*\*

# 2\. Click \*\*Generate Research Analysis\*\*

# 3\. The AI agents will generate:

# 

# &#x20;  \* Research keywords

# &#x20;  \* Literature review

# &#x20;  \* Research gaps

# &#x20;  \* Grant proposal

# 

# \---

# 

# \# Example Input

# 

# ```

# Multimodal Sentiment Analysis using Audio and Text

# ```

# 

# \---

# 

# \# Example Output

# 

# The system generates:

# 

# \* Literature Review

# \* Research Gap Analysis

# \* Proposed Methodology

# \* Expected Outcomes

# \* Grant Proposal Draft

# 

# \---

# 

# \# Project Structure

# 

# ```

# research-assistant

# │

# ├── agents

# │   └── agents.py

# │

# ├── tasks

# │   └── tasks.py

# │

# ├── rag

# │   ├── retriever.py

# │

# ├── ui

# │   └── app.py

# │

# ├── config.py

# ├── main.py

# ├── requirements.txt

# ├── README.md

# ```

# 

# \---

# 

# \# Notes

# 

# \* The system runs \*\*locally using Ollama\*\*, so no paid API is required.

# \* Model performance depends on your machine specifications.

# \* Larger models may take longer to generate responses.

# 

# \---

# 

# \# Future Improvements

# 

# \* Real-time academic paper retrieval (ArXiv / Semantic Scholar)

# \* Citation generation

# \* PDF export for research reports

# \* Automatic PowerPoint generation

# \* Improved RAG dataset

# 

# \---



