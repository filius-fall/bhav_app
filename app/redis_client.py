import os
from pathlib import Path

import redis
from dotenv import load_dotenv

load_dotenv()

env_path = Path('..')/'.env'
host = os.getenv("REDIS_HOST")
port = os.getenv("REDIS_PORT")
db = os.getenv("REDIS_DB")
username = os.getenv("REDIS_USERNAME")
password = os.getenv("REDIS_PASSWORD")
test = os.getenv("TEST")

class RedisClient:

    def connect(self, decode_response = False):
        print("ITS TESTING TIME KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK-------LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
        print(test)
        return redis.StrictRedis(
            host = host,
            db = db,
            port = port,
            username = username,
            password = password,
        )