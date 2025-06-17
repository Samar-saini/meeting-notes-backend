import hashlib
import os
import redis
from transformers import pipeline

# Set environment variables
os.environ["TRANSFORMERS_NO_TF"] = "1"

# Connect to Redis
REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
redis_client = redis.from_url(REDIS_URL)

# Load the Hugging Face summarization pipeline (only once)
print("📦 Loading summarization model...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
print("✅ Model loaded")

def summarize_text(transcript: str) -> str:
    # Clean and truncate input
    max_input_words = 1024
    transcript = transcript.strip().replace('\n', ' ')
    words = transcript.split()
    if len(words) > max_input_words:
        transcript = ' '.join(words[:max_input_words])

    # Generate cache key
    cache_key = hashlib.sha256(transcript.encode()).hexdigest()

    # Check Redis cache
    cached_summary = redis_client.get(cache_key)
    if cached_summary:
        print("✅ Using cached summary")
        return cached_summary.decode("utf-8")

    # Run summarization
    print("🟡 Running summarization...")
    summary = summarizer(transcript, max_length=200, min_length=50, do_sample=False)[0]['summary_text']

    # Save in cache
    redis_client.set(cache_key, summary)
    print("📝 New summary cached")

    return summary
