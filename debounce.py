import threading
from functools import wraps


def debounce(wait):
    """Postpone a function call until `wait` seconds have elapsed since the
    last invocation. Useful for rate-limiting noisy callbacks."""
    def decorator(fn):
        timer = None

        @wraps(fn)
        def debounced(*args, **kwargs):
            nonlocal timer
            if timer is not None:
                timer.cancel()
            timer = threading.Timer(wait, lambda: fn(*args, **kwargs))
            timer.start()
        return debounced
    return decorator
