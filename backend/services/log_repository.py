from datetime import datetime
from bson import ObjectId
from models.schemas import Log, LogCreate
from models.database import get_logs_collection
from typing import List, Optional


class LogRepository:
    """Log repository for CRUD operations"""
    
    @staticmethod
    def create(log_data: LogCreate) -> Log:
        """Create a new log entry"""
        collection = get_logs_collection()
        
        doc = {
            "agent": log_data.agent,
            "action": log_data.action,
            "reason": log_data.reason,
            "timestamp": datetime.utcnow()
        }
        
        result = collection.insert_one(doc)
        doc["_id"] = str(result.inserted_id)
        
        return Log(**doc)
    
    @staticmethod
    def get_all() -> List[Log]:
        """Get all logs, sorted by timestamp descending"""
        collection = get_logs_collection()
        logs = []
        
        for doc in collection.find().sort("timestamp", -1):
            doc["_id"] = str(doc["_id"])
            logs.append(Log(**doc))
        
        return logs
    
    @staticmethod
    def get_by_agent(agent_name: str) -> List[Log]:
        """Get logs by agent"""
        collection = get_logs_collection()
        logs = []
        
        for doc in collection.find({"agent": agent_name}).sort("timestamp", -1):
            doc["_id"] = str(doc["_id"])
            logs.append(Log(**doc))
        
        return logs
    
    @staticmethod
    def delete_all() -> int:
        """Delete all logs (useful for testing)"""
        collection = get_logs_collection()
        result = collection.delete_many({})
        return result.deleted_count
