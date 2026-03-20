import arxiv  #for paper fetching from arXiv(python librery)

def fetch_papers(query, max_results=5): #function to fetch papers from arXiv
    search = arxiv.Search(     #search object
        query=query,
        max_results=max_results, 
        sort_by=arxiv.SortCriterion.Relevance  #sort by relevance
    )

    papers = []  #list to store the papers

    for result in search.results():  #search results(iterates like for 5 papers need to loop 5 times)
        paper = f"""
Title: {result.title}

Summary:
{result.summary}
"""  #f-string to format the paper
        papers.append(paper)  #append the paper to the list

    return papers  #return the list of papers