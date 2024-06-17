import solve_2017_03 as subject
import pytest

def test_manhattan_distance():
    assert subject.manhattan_distance(1) == 0
    assert subject.manhattan_distance(12) == 3
    assert subject.manhattan_distance(23) == 2
    assert subject.manhattan_distance(1024) == 31

def test_get_first_over():
    assert subject.get_first_over(20) == 23
    assert subject.get_first_over(100) == 122
    assert subject.get_first_over(200) == 304
    assert subject.get_first_over(300) == 304
    assert subject.get_first_over(400) == 747
    assert subject.get_first_over(500) == 747
    assert subject.get_first_over(600) == 747
    assert subject.get_first_over(700) == 747
    assert subject.get_first_over(800) == 806
    
