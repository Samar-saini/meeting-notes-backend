import redis
import hashlib
from app.config import REDIS_URL

redis_client = redis.Redis.from_url(REDIS_URL)

def generate_cache_key(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def get_cached_summary(text: str) -> str | None:
    key = generate_cache_key(text)
    return redis_client.get(key)

def set_cached_summary(text: str, summary: str):
    key = generate_cache_key(text)
    redis_client.set(key, summary, ex=3600)  # expires in 1 hour
