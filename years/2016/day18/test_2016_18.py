import solve_2016_18 as subject
import pytest

def test_get_safe_tiles():
    assert subject.get_safe_tiles('..^^.', 3) == 6
    assert subject.get_safe_tiles('.^^.^.^^^^', 10) == 38


