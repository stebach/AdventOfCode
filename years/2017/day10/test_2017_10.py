import solve_2017_10 as subject
import pytest

def test_get_hash():
    assert subject.get_hash([3, 4, 1, 5], 5) == [3,4,2,1,0]

def test_knot_hash():
    assert subject.get_knot_hash('') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert subject.get_knot_hash('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert subject.get_knot_hash('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert subject.get_knot_hash('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'


