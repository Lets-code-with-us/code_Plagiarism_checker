from database.redis import r,get_vectors
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle
from modules.preprocess import preprocess_query_code


def score_it(key:str,code:str,vectorize,language:int):
    k = key.split(":")[0]+":*"
    vector_list = get_vectors(k)    
    sim = []
    pre_code = preprocess_query_code(code,language)
    query_vec = vectorize.transform([pre_code])
    for i in vector_list:
        tfidf_matrix = pickle.loads(i)
        similarities = cosine_similarity(query_vec, tfidf_matrix)[0][0]
        similarities = np.clip(similarities, 0, 1)   
        sim.append(similarities)
      
    print(max(sim) * 100)
    # print(max(np.concatenate(sim)) * 100)