from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    """Task status enum"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"


class TaskPriority(str, Enum):
    """Task priority enum"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class TaskBase(BaseModel):
    """Base task schema"""
    title: str = Field(..., min_length=1, max_length=255)
    owner: str = Field(..., min_length=1, max_length=100)
    deadline: str  # ISO format: YYYY-MM-DD or timestamp
    status: TaskStatus = TaskStatus.PENDING
    priority: TaskPriority = TaskPriority.MEDIUM


class TaskCreate(TaskBase):
    """Schema for creating a task"""
    pass


class Task(TaskBase):
    """Full task schema (with DB fields)"""
    id: str = Field(alias="_id")
    created_at: datetime


class LogBase(BaseModel):
    """Base log schema"""
    agent: str = Field(..., min_length=1, max_length=100)
    action: str = Field(..., min_length=1, max_length=500)
    reason: str = Field(..., min_length=1, max_length=1000)


class LogCreate(LogBase):
    """Schema for creating a log"""
    pass


class Log(LogBase):
    """Full log schema (with DB fields)"""
    id: str = Field(alias="_id")
    timestamp: datetime


class ProcessRequest(BaseModel):
    """Request schema for POST /process"""
    input: str = Field(..., min_length=1)


class ProcessResponse(BaseModel):
    """Response schema for POST /process"""
    tasks: List[Task]
    logs: List[Log]


class ErrorResponse(BaseModel):
    """Error response schema"""
    error: str
    details: Optional[str] = None
