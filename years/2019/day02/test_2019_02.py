import solve_2019_02 as subject
import pytest

def test_intcode():
    assert subject.intcode([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50]
    assert subject.intcode([1,0,0,0,99]) == [2,0,0,0,99]
    assert subject.intcode([2,3,0,3,99]) == [2,3,0,6,99]
    assert subject.intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert subject.intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

