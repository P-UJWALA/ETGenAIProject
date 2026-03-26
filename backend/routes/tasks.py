from fastapi import APIRouter, HTTPException
from models.schemas import Task
from services.task_repository import TaskRepository
from typing import List

router = APIRouter(prefix="/api", tags=["tasks"])


@router.get("/tasks", response_model=List[Task])
async def get_tasks():
    """
    Retrieve all tasks from database.
    
    Returns:
        List of all tasks
    """
    try:
        tasks = TaskRepository.get_all()
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve tasks")


@router.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: str):
    """
    Retrieve a specific task by ID.
    
    Args:
        task_id: Task MongoDB ObjectId (as string)
        
    Returns:
        Task object if found, 404 if not
    """
    try:
        task = TaskRepository.get_by_id(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve task")
