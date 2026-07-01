"""Safe nested lookup by dotted path: deep_get(d, "a.b.0.c")."""


def deep_get(obj, path, default=None):
    for key in path.split("."):
        if isinstance(obj, dict) and key in obj:
            obj = obj[key]
        elif isinstance(obj, (list, tuple)):
            try:
                obj = obj[int(key)]
            except (ValueError, IndexError):
                return default
        else:
            return default
    return obj


if __name__ == "__main__":
    d = {"a": {"b": [{"c": 1}]}}
    assert deep_get(d, "a.b.0.c") == 1
    assert deep_get(d, "a.x.y", "z") == "z"
    print("ok")
