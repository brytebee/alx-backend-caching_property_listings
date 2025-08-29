from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection

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
