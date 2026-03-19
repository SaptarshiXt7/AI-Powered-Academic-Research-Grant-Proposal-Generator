from crewai import Task
from agents.agents import research_agent, literature_agent, gap_agent, proposal_agent


research_task = Task(
    description="""
Analyze the research topic: {topic}

Generate:
1. Important research keywords
2. Possible research directions
3. Relevant subtopics

Ensure the output is clearly structured.
""",
    expected_output="""
A structured list of keywords and research directions related to the topic.
""",
    agent=research_agent
)


literature_task = Task(
    description="""
Using the research topic {topic} and the retrieved research paper context {context},

Write a literature review including:
- Key existing research
- Important findings
- Common methodologies used
- Current research trends

Ensure the literature review is clear and well structured.
""",
    expected_output="""
A structured literature review summarizing the most relevant research work.
""",
    agent=literature_agent
)


gap_task = Task(
    description="""
Based on the literature review for the research topic {topic},

Identify:
- Key research gaps
- Limitations in existing studies
- Areas needing further investigation
""",
    expected_output="""
A list of clear research gaps and opportunities for future research.
""",
    agent=gap_agent
)


proposal_task = Task(
    description="""
Using the research topic {topic}, literature review, and identified research gaps,

Write a structured research grant proposal including:

1. Title
2. Abstract
3. Problem Statement
4. Literature Background
5. Proposed Methodology
6. Expected Results
7. Research Impact
8. Conclusion

Ensure the proposal is well structured and academic in tone.
""",
    expected_output="""
A complete research grant proposal document with clearly separated sections.
""",
    agent=proposal_agent
)