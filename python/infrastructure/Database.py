from pymongo import MongoClient


class DatabaseConnection:
    def __init__(self, mongo_uri: str, database_name: str):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[database_name]

