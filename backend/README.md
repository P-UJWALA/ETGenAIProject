# ET GenAI Backend - Development Setup

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup MongoDB
Make sure MongoDB is running locally or update `MONGO_URI` in `.env`

```bash
# If using Docker:
docker run -d -p 27017:27017 --name mongodb mongo:latest
```

### 3. Create .env file
```bash
cp .env.example .env
# Edit .env with your configuration
```

### 4. Run the server
```bash
python main.py
```

Server will start at `http://localhost:8000`

---

## API Documentation

### Available Endpoints

**Health Check**
- `GET /health` - Check server status

**Process (Core)**
- `POST /api/process` - Process input and generate tasks

**Tasks**
- `GET /api/tasks` - Get all tasks
- `GET /api/tasks/{task_id}` - Get specific task

**Logs**
- `GET /api/logs` - Get all decision logs
- `GET /api/logs/agent/{agent_name}` - Get logs from specific agent

---

## Interactive API Docs
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## Project Structure
```
backend/
├── main.py                 # FastAPI app entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
│
├── models/
│   ├── schemas.py        # Pydantic request/response schemas
│   └── database.py       # MongoDB connection & collections
│
├── services/
│   ├── orchestrator.py   # Orchestration logic (stub)
│   ├── task_repository.py # Task CRUD operations
│   └── log_repository.py  # Log CRUD operations
│
├── routes/
│   ├── process.py        # POST /process route
│   ├── tasks.py          # Task endpoints
│   └── logs.py           # Log endpoints
│
├── agents/               # Placeholder for AI agents
│   └── (to be implemented by teammate)
│
└── orchestrator/         # Placeholder for orchestration
    └── (to be implemented by teammate)
```

---

## API Contract

### POST /process
**Request:**
```json
{
  "input": "meeting transcript or task description"
}
```

**Response:**
```json
{
  "tasks": [
    {
      "id": "507f1f77bcf86cd799439011",
      "title": "Task title",
      "owner": "Owner name",
      "deadline": "2024-04-15T10:30:00",
      "status": "pending",
      "priority": "high",
      "created_at": "2024-03-26T10:30:00"
    }
  ],
  "logs": [
    {
      "id": "507f1f77bcf86cd799439012",
      "agent": "parser_agent",
      "action": "Extract tasks from input",
      "reason": "Initial parsing of meeting transcript",
      "timestamp": "2024-03-26T10:30:00"
    }
  ]
}
```

### GET /api/tasks
**Response:** Array of Task objects

### GET /api/logs
**Response:** Array of Log objects (sorted by timestamp, newest first)

---

## Testing

### Using cURL
```bash
# Process a request
curl -X POST http://localhost:8000/api/process \
  -H "Content-Type: application/json" \
  -d '{"input": "Team meeting: Need to complete report by Friday"}'

# Get all tasks
curl http://localhost:8000/api/tasks

# Get all logs
curl http://localhost:8000/api/logs

# Health check
curl http://localhost:8000/health
```

### Using Postman/Insomnia
Use the Swagger UI at `/docs` for interactive testing

---

## Next Steps for Teammate (AI Agent Implementation)

Implement in `services/orchestrator.py`:
1. **Parser Agent** - Extract tasks from input text
2. **Planner Agent** - Assign owners, deadlines, priorities
3. **Monitor Agent** - Detect delays and suggest actions

Keep the interface unchanged:
```python
def run(input_text: str) -> Tuple[List[Task], List[Log]]:
    # Your implementation here
    pass
```

---

## Troubleshooting

**MongoDB Connection Error**
- Ensure MongoDB is running
- Check `MONGO_URI` in `.env`

**CORS Error**
- Verify frontend origin is in `CORS_ORIGINS`
- Check `.env` configuration

**Port in Use**
- Change `API_PORT` in `.env`
- Or kill process on port 8000

---

## Development Notes

- Database schema is auto-managed by PyMongo
- All timestamps are UTC
- Task IDs and Log IDs are MongoDB ObjectIds converted to strings
- Error responses include optional `details` field

