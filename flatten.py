def flatten(nested):
    """Recursively flatten an arbitrarily nested iterable of values into a
    single flat list. Strings/bytes are treated as scalars."""
    out = []
    for item in nested:
        if hasattr(item, "__iter__") and not isinstance(item, (str, bytes)):
            out.extend(flatten(item))
        else:
            out.append(item)
    return out
