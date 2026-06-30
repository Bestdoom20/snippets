from functools import wraps


def memoize(fn):
    """Cache results keyed by positional + keyword args. A tiny, dependency-free
    alternative to functools.lru_cache when you want an inspectable cache."""
    cache = {}

    @wraps(fn)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = fn(*args, **kwargs)
        return cache[key]

    wrapper.cache = cache
    return wrapper
