from datetime import datetime
from bson import ObjectId
from models.schemas import Task, TaskCreate, TaskStatus, TaskPriority
from models.database import get_tasks_collection
from typing import List, Optional


class TaskRepository:
    """Task repository for CRUD operations"""
    
    @staticmethod
    def create(task_data: TaskCreate) -> Task:
        """Create a new task"""
        collection = get_tasks_collection()
        
        doc = {
            "title": task_data.title,
            "owner": task_data.owner,
            "deadline": task_data.deadline,
            "status": task_data.status.value,
            "priority": task_data.priority.value,
            "created_at": datetime.utcnow()
        }
        
        result = collection.insert_one(doc)
        doc["_id"] = str(result.inserted_id)
        
        return Task(**doc)
    
    @staticmethod
    def get_all() -> List[Task]:
        """Get all tasks"""
        collection = get_tasks_collection()
        tasks = []
        
        for doc in collection.find():
            doc["_id"] = str(doc["_id"])
            tasks.append(Task(**doc))
        
        return tasks
    
    @staticmethod
    def get_by_id(task_id: str) -> Optional[Task]:
        """Get task by ID"""
        collection = get_tasks_collection()
        
        try:
            doc = collection.find_one({"_id": ObjectId(task_id)})
            if doc:
                doc["_id"] = str(doc["_id"])
                return Task(**doc)
        except Exception:
            pass
        
        return None
    
    @staticmethod
    def update(task_id: str, task_data: dict) -> Optional[Task]:
        """Update a task"""
        collection = get_tasks_collection()
        
        try:
            result = collection.update_one(
                {"_id": ObjectId(task_id)},
                {"$set": task_data}
            )
            
            if result.modified_count > 0:
                return TaskRepository.get_by_id(task_id)
        except Exception:
            pass
        
        return None
    
    @staticmethod
    def delete(task_id: str) -> bool:
        """Delete a task"""
        collection = get_tasks_collection()
        
        try:
            result = collection.delete_one({"_id": ObjectId(task_id)})
            return result.deleted_count > 0
        except Exception:
            return False
