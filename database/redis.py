import redis
import os 
from dotenv import load_dotenv
load_dotenv()
URL = str(os.getenv('REDISURL'))
r = redis.Redis.from_url(URL)



def store_vector(key:str,vector):
    r.set(key,vector)
    
    
def get_vectors(key:str):
    keys = []
    for k in r.scan_iter(key):
        value = r.get(k)
        if value is not None:
            keys.append(value)
    return keys
