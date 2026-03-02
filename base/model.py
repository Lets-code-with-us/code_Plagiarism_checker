from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def vectorization_code(corpus):
    vectorize = TfidfVectorizer(
        token_pattern=r'\b\w+\b',
        lowercase=True
    )
    tdif_matrix = vectorize.fit_transform(corpus)
    return vectorize,tdif_matrix


def search(query_code, vectorizer, tfidf_matrix):
    query_vec = vectorizer.transform([query_code])
    similarities = cosine_similarity(query_vec, tfidf_matrix)[0]
    similarities = np.clip(similarities, 0, 1)
    return max(similarities * 100)
    
    