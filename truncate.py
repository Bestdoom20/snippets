"""Truncate to n chars on a word boundary with an ellipsis."""


def truncate(text, n, suffix="…"):
    if len(text) <= n:
        return text
    cut = text[: n - len(suffix)].rstrip()
    if " " in cut:
        cut = cut.rsplit(" ", 1)[0].rstrip()
    return cut + suffix


if __name__ == "__main__":
    assert truncate("hello world foo", 11) == "hello…"
    assert truncate("short", 10) == "short"
    print("ok")
