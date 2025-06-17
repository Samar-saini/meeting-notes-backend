from fastapi import FastAPI
from app.schemas import SummarizationRequest, TaskStatus
from app.tasks import summarize_meeting, celery_app
from celery.result import AsyncResult

app = FastAPI()

@app.post("/summarize", response_model=TaskStatus)
def submit_summary(request: SummarizationRequest):
    task = summarize_meeting.delay(request.transcript)
    return {"task_id": task.id, "status": "processing"}

@app.get("/result/{task_id}", response_model=TaskStatus)
def get_summary_result(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    if result.ready():
        return {
            "task_id": task_id,
            "status": "completed",
            "result": result.result
        }
    return {"task_id": task_id, "status": "processing"}
