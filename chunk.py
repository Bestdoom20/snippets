"""Split an iterable into fixed-size chunks."""
from itertools import islice


def chunk(it, size):
    it = iter(it)
    while batch := list(islice(it, size)):
        yield batch
