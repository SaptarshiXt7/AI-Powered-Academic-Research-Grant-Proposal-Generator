from crewai import Agent, LLM

# Use Ollama's OpenAI-compatible API endpoint
llm = LLM(
    model="llama3",
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Ollama doesn't need a real key, but the OpenAI client requires one
)

research_agent = Agent(
    role="Research Analyst",
    goal="Analyze research topics and produce literature reviews",
    backstory="You are an expert academic researcher who analyzes topics and summarizes research papers.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

proposal_agent = Agent(
    role="Grant Proposal Writer",
    goal="Write professional research grant proposals",
    backstory="You are an expert grant proposal writer for academic research projects.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)