import os
from pymongo import MongoClient


class Config:
    token = os.environ['TOKEN']

    @classmethod
    def connect_to_mongo(cls):
        uri = os.environ['MONGO_URI']
        client = MongoClient(uri)
        return client

