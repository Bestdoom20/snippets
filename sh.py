"""Run a command, return stripped stdout; raise on non-zero exit."""
import subprocess


def sh(*args, **kw):
    return subprocess.run(
        args, capture_output=True, text=True, check=True, **kw
    ).stdout.strip()


if __name__ == "__main__":
    assert sh("echo", "hi") == "hi"
    print("ok")
