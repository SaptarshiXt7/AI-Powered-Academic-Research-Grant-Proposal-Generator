from crewai import Crew
from agents.agents import research_agent, literature_agent, gap_agent, proposal_agent
from tasks.tasks import research_task, literature_task, gap_task, proposal_task
from rag.ingest import fetch_papers
from rag.retriever import build_vector_db, retrieve_docs


def run_pipeline(topic):

    papers = fetch_papers(topic)

    db = build_vector_db(papers)

    context = retrieve_docs(db, topic)

    crew = Crew(
        agents=[
            research_agent,
            literature_agent,
            gap_agent,
            proposal_agent
        ],
        tasks=[
            research_task,
            literature_task,
            gap_task,
            proposal_task
        ],
        verbose=True
    )

    result = crew.kickoff(inputs={
        "topic": topic,
        "context": context
    })

    return result.raw