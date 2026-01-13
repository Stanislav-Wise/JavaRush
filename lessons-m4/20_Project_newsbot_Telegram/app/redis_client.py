from redis import Redis
from redis.exceptions import RedisError

from app.config import settings


def get_redis_client() -> Redis:
    client = Redis.from_url(settings.redis_url, decode_responses=True)

    return client


def ping_redis() -> bool:
    try:
        client = get_redis_client()
        result = client.ping()
        return bool(result)

    except RedisError:
        return False

