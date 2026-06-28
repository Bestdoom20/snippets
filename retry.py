"""Retry a flaky call with exponential backoff. Stdlib only."""
import time, functools


def retry(times=3, base=0.2, exc=Exception):
    def deco(fn):
        @functools.wraps(fn)
        def wrap(*a, **k):
            for i in range(times):
                try:
                    return fn(*a, **k)
                except exc:
                    if i == times - 1:
                        raise
                    time.sleep(base * 2 ** i)
        return wrap
    return deco
