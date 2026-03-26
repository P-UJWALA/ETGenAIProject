from pymongo import MongoClient
from pymongo.collection import Collection
from config import settings
from typing import Optional

# Global MongoDB connection
_client: Optional[MongoClient] = None
_db = None


def connect_db():
    """Initialize MongoDB connection"""
    global _client, _db
    try:
        _client = MongoClient(settings.MONGO_URI)
        _db = _client[settings.DATABASE_NAME]
        # Test connection
        _client.admin.command("ping")
        print(f"✓ Connected to MongoDB: {settings.DATABASE_NAME}")
    except Exception as e:
        print(f"✗ Failed to connect to MongoDB: {e}")
        raise


def disconnect_db():
    """Close MongoDB connection"""
    global _client
    if _client:
        _client.close()
        print("✓ MongoDB connection closed")


def get_db():
    """Get database instance"""
    if _db is None:
        connect_db()
    return _db


def get_tasks_collection() -> Collection:
    """Get tasks collection"""
    db = get_db()
    return db[settings.TASKS_COLLECTION]


def get_logs_collection() -> Collection:
    """Get logs collection"""
    db = get_db()
    return db[settings.LOGS_COLLECTION]
