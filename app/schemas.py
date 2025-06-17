from pydantic import BaseModel
from typing import Optional

class SummarizationRequest(BaseModel):
    transcript: str

class TaskStatus(BaseModel):
    task_id: str
    status: str
    result: Optional[str] = None
