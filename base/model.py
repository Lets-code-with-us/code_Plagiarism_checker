from sklearn.feature_extraction.text import TfidfVectorizer


def vectorization_code(corpus):
    vectorize = TfidfVectorizer(
        token_pattern=r'\b\w+\b',
        lowercase=True
    )
    tdif_matrix = vectorize.fit_transform(corpus)
    return vectorize,tdif_matrix
    
    