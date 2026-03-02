from pydantic import BaseModel


class Code(BaseModel):
    language:int
    code:str