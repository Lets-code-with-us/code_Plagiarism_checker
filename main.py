from fastapi import FastAPI
from modules.preprocess import preprocess_code 
from model.code import Code
from base.model import vectorization_code,search




app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/")
def manage_file(code:Code):
    copus = preprocess_code(code.language,code.code)
    vectorize,tdif_matrix = vectorization_code(copus)
    score = search("#include <stdio.h> int main() {\n    int n;\n    printf(\"Enter a number: \");\n    scanf(\"%d\", &n);\n    if(n % 2 == 0) {\n        printf(\"%d is Even\\n\", n);} else {\n        printf(\"%d is Odd\\n\", n);}\n    return 0;\n}",vectorizer=vectorize,tfidf_matrix=tdif_matrix)
    print(score)
    return {"message":"Done"}


# 58.20979882293952
# 59.76497514156036