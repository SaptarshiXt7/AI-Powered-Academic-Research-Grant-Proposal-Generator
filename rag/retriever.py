from sklearn.feature_extraction.text import TfidfVectorizer  #for vectorization(converting text to numbers)
import numpy as np  #for numerical operations

def build_vector_db(papers):  #function to build the vector database(for storing the paper list)

    vectorizer = TfidfVectorizer(stop_words="english")  #object vectorizer to convert text to numbers

    X = vectorizer.fit_transform(papers)  #[X -->  SPARSH MATRIX] (fit-> learn vocab, transform-> convert to numbers)

    db = {
        "vectorizer": vectorizer,
        "matrix": X,
        "papers": papers
    }

    return db #dictionary


def retrieve_docs(db, query):  #function to retrieve the documents(based on user query)

    vectorizer = db["vectorizer"]  #vectorizer to convert text to numbers (query)
    matrix = db["matrix"]  #sparse matrix
    papers = db["papers"]  #list of papers

    query_vec = vectorizer.transform([query])  #query-->numbers

    scores = (matrix * query_vec.T).toarray()  # DOT MATRIX MULTIPLICATION --> similarity scores

    top_indices = np.argsort(scores[:,0])[-3:]  #top 3 indices

    results = [papers[i] for i in top_indices]  #top 3 papers

    context = "\n".join(results)  #join the top 3 papers

    return context  #return the context