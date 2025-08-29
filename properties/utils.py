# properties/utils.py
from django.core.cache import cache
from django_redis import get_redis_connection
import logging
from .models import Property

logger = logging.getLogger(__name__)

def get_all_properties():
    properties = cache.get("all_properties")
    if not properties:
        properties = list(Property.objects.all())
        cache.set("all_properties", properties, 3600)  # 1 hour
    return properties

def get_redis_cache_metrics():
    r = get_redis_connection("default")
    info = r.info("stats")
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    ratio = hits / (hits + misses) if (hits + misses) > 0 else 0
    return {"hits": hits, "misses": misses, "hit_ratio": ratio}

def calculate_hit_ratio(cache_hits: int, total_requests: int) -> float:
    """
    Calculate the cache hit ratio.
    Logs metrics and handles errors gracefully.
    """
    try:
        hit_ratio = (cache_hits / total_requests) if total_requests > 0 else 0
        logger.info(
            f"Cache Metrics -> Hits: {cache_hits}, Total Requests: {total_requests}, Hit Ratio: {hit_ratio:.2f}"
        )
        return hit_ratio
    except Exception as e:
        logger.error(f"Error calculating hit ratio: {e}")
        return 0
