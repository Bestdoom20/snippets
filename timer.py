"""Context manager that prints elapsed wall time."""
import time, contextlib


@contextlib.contextmanager
def timer(label="block"):
    t = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label}: {time.perf_counter() - t:.3f}s")
