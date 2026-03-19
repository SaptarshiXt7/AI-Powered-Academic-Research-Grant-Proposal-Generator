from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def build_vector_db(papers):

    vectorizer = TfidfVectorizer(stop_words="english")

    X = vectorizer.fit_transform(papers)

    db = {
        "vectorizer": vectorizer,
        "matrix": X,
        "papers": papers
    }

    return db


def retrieve_docs(db, query):

    vectorizer = db["vectorizer"]
    matrix = db["matrix"]
    papers = db["papers"]

    query_vec = vectorizer.transform([query])

    scores = (matrix * query_vec.T).toarray()

    top_indices = np.argsort(scores[:,0])[-3:]

    results = [papers[i] for i in top_indices]

    context = "\n".join(results)

    return context