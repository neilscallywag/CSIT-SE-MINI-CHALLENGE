from dotenv import load_dotenv
import os

load_dotenv("./.env")
MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_FLIGHTS = os.getenv("COLLECTION_FLIGHTS")
COLLECTION_HOTELS = os.getenv("COLLECTION_HOTELS")
