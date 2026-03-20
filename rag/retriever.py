from sklearn.feature_extraction.text import TfidfVectorizer  #for vectorization(converting text to numbers)
import numpy as np  #for numerical operations

#AI WORKS WELL IN NUMBERS, NOT IN WORDS SO WE NEED TO CONVERT THE TEXT DATA INTO NUMBERS


def build_vector_db(papers):  #WEEK ON DEEP SEMNTIC SIMILARTY

    vectorizer = TfidfVectorizer(stop_words="english")  #USE FILTER FOR REMOVING COMMON WORDS

    X = vectorizer.fit_transform(papers)  #[X -->  SPARSH MATRIX] (fit-> learn vocab, transform-> convert to numbers)

    db = {
        "vectorizer": vectorizer,
        "matrix": X,
        "papers": papers
    }

    return db #dictionary


def retrieve_docs(db, query):  #function to retrieve the documents(based on user query)

                #USER QUERY --> VECTORIZATION

    vectorizer = db["vectorizer"]  
    matrix = db["matrix"]  
    papers = db["papers"]  

    query_vec = vectorizer.transform([query])  #query-->numbers

    scores = (matrix * query_vec.T).toarray()  # DOT MATRIX MULTIPLICATION --> similarity scores

    top_indices = np.argsort(scores[:,0])[-3:]  #top 3 indices

    results = [papers[i] for i in top_indices]  #top 3 papers SELECTED

    context = "\n".join(results)  #join the top 3 papers

    return context  #return the context