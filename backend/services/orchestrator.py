from typing import Tuple, List
from models.schemas import Task, Log, TaskCreate, LogCreate, TaskStatus, TaskPriority
from services.task_repository import TaskRepository
from services.log_repository import LogRepository
from datetime import datetime, timedelta


class OrchestratorService:
    """
    Orchestrator service that coordinates the workflow:
    1. Parser Agent (extract tasks from input)
    2. Planner Agent (assign owner, deadline, priority)
    3. Monitor Agent (detect delays, log decisions)
    
    STUB IMPLEMENTATION - Teammate will replace internal logic
    """
    
    @staticmethod
    def run(input_text: str) -> Tuple[List[Task], List[Log]]:
        """
        Main orchestration entry point.
        
        Args:
            input_text: Meeting transcript or task description
            
        Returns:
            Tuple of (tasks, logs) from orchestration process
        """
        logs = []
        tasks = []
        
        try:
            # PHASE 1: Parser Agent (STUB)
            # In production: Parse input_text to extract task titles
            parser_log = LogCreate(
                agent="parser_agent",
                action="Extract tasks from input",
                reason="Initial parsing of meeting transcript"
            )
            logs.append(LogRepository.create(parser_log))
            
            # Stub: Create 1-2 sample tasks for demo
            sample_tasks = [
                {
                    "title": f"Task extracted from input: {input_text[:50]}...",
                    "owner": "To be assigned",
                    "deadline": (datetime.utcnow() + timedelta(days=7)).isoformat(),
                    "status": TaskStatus.PENDING,
                    "priority": TaskPriority.MEDIUM
                }
            ]
            
            # PHASE 2: Planner Agent (STUB)
            # In production: Assign owners, deadlines, priorities
            planner_log = LogCreate(
                agent="planner_agent",
                action="Assign owner, deadline, priority",
                reason="Planning task execution based on input context"
            )
            logs.append(LogRepository.create(planner_log))
            
            # Create tasks from samples
            for task_data in sample_tasks:
                task_create = TaskCreate(**task_data)
                created_task = TaskRepository.create(task_create)
                tasks.append(created_task)
            
            # PHASE 3: Monitor Agent (STUB)
            # In production: Detect delays, suggest actions
            monitor_log = LogCreate(
                agent="monitor_agent",
                action="Monitor task execution status",
                reason="Check for delays or blockers"
            )
            logs.append(LogRepository.create(monitor_log))
            
            return tasks, logs
            
        except Exception as e:
            # Log error
            error_log = LogCreate(
                agent="orchestrator",
                action="Error occurred during orchestration",
                reason=str(e)
            )
            logs.append(LogRepository.create(error_log))
            
            raise
