from crewai import Crew
from agents import research_agent, proposal_agent
from tasks import research_task, proposal_task

crew = Crew(
    agents=[research_agent, proposal_agent],
    tasks=[research_task, proposal_task],
    verbose=True
)