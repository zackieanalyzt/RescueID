from sqlalchemy import create_engine
from pymongo import MongoClient

# PostgreSQL Configuration
def get_postgresql_engine():
    DATABASE_URI = "postgresql://username:password@localhost:5432/rescueid"
    return create_engine(DATABASE_URI)

# MongoDB Configuration
def get_mongodb_client():
    client = MongoClient("mongodb://localhost:27017/")
    return client["rescueid"]
