from celery import Celery
from app.summarizer import summarize_text
from app.cache import get_cached_summary, set_cached_summary
from app.config import REDIS_URL

celery_app = Celery("tasks", broker=REDIS_URL, backend=REDIS_URL)

@celery_app.task()
def summarize_meeting(transcript: str) -> str:
    print("📥 Task received for summarization")

    cached = get_cached_summary(transcript)
    if cached:
        print("✅ Returning cached summary")
        return cached.decode()

    summary = summarize_text(transcript)
    set_cached_summary(transcript, summary)

    print("📤 Task completed and cached")
    return summary
