import arxiv

def fetch_papers(query, max_results=5):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    papers = []

    for result in search.results():
        paper = f"""
Title: {result.title}

Summary:
{result.summary}
"""
        papers.append(paper)

    return papers