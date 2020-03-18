from joins_and_splits import agg_texts
import pytest


def test_agg_texts():
    x, y, _ = agg_texts(['sachs', 'huch'])
    assert x.shape[0] == y.shape[0]
