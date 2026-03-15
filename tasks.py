from crewai import Task
from agents import research_agent, proposal_agent

research_task = Task(
    description="Analyze the research topic: {topic} and create a literature review and research gap.",
    agent=research_agent,
    expected_output="Literature review and research gap analysis"
)

proposal_task = Task(
    description="Write a grant proposal based on the research analysis of {topic}.",
    agent=proposal_agent,
    expected_output="Complete research grant proposal"
)