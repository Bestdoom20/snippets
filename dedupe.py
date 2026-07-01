"""Order-preserving dedupe; optional key function."""


def dedupe(items, key=None):
    seen = set()
    out = []
    for x in items:
        k = key(x) if key else x
        if k not in seen:
            seen.add(k)
            out.append(x)
    return out


if __name__ == "__main__":
    assert dedupe([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert dedupe(["Aa", "aA", "b"], key=str.lower) == ["Aa", "b"]
    print("ok")
