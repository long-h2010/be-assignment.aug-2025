import redis
import os

r = redis.Redis(host=os.getenv("REDIS_HOST","redis"), port=int(os.getenv("REDIS_PORT","6379")), db=0)

def cache_key_tasks(project_id: int, **filters):
    parts = [f"{k}={v}" for k, v in sorted(filters.items()) if v is not None]
    return f"Tasks:{project_id}:" + "|".join(parts)

def invalidate_project_tasks(project_id: int):
    for k in r.scan_iter(f"Tasks:{project_id}:*"):
        r.delete(k)
