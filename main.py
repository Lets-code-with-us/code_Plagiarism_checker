from fastapi import FastAPI
from modules.preprocess import preprocess_code 
from model.code import Code
from base.model import vectorization_code
from database.redis import store_vector
from modules.score import score_it
import pickle

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/vectorized")
async def vectorized(code:Code):
    copus,id = preprocess_code(code.language,code.code)
    vectorize,tdif_matrix = vectorization_code(copus)
    store_vector(code.uniqueid,pickle.dumps(tdif_matrix))
    score_it(code.uniqueid,code.code,vectorize,code.language)
    return {"message":"Done"}
