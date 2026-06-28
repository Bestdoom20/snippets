"""URL-safe slug from arbitrary text. Stdlib only."""
import re, unicodedata


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_-]+", "-", text)


if __name__ == "__main__":
    assert slugify("Hello,  World!") == "hello-world"
    assert slugify("Café del Mar") == "cafe-del-mar"
    print("ok")
