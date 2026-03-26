from fastapi import APIRouter, HTTPException
from models.schemas import ProcessRequest, ProcessResponse, ErrorResponse
from services.orchestrator import OrchestratorService

router = APIRouter(prefix="/api", tags=["process"])


@router.post("/process", response_model=ProcessResponse)
async def process(request: ProcessRequest):
    """
    Main endpoint to process meeting transcripts and generate tasks.
    
    - Receives input (meeting transcript or task description)
    - Calls orchestrator (parser → planner → monitor)
    - Stores tasks and logs in database
    - Returns structured response
    """
    try:
        # Validate input
        if not request.input or not request.input.strip():
            raise HTTPException(status_code=400, detail="Input cannot be empty")
        
        # Call orchestrator
        tasks, logs = OrchestratorService.run(request.input)
        
        # Return response
        return ProcessResponse(tasks=tasks, logs=logs)
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
