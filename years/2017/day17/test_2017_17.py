import solve_2017_17 as subject
import pytest

def test_spinlock():
    assert subject.spinlock(3) == 638


