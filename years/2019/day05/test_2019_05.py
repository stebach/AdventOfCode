import solve_2019_05 as subject
import pytest


def test_intcode():
    assert subject.intcode([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50]
    assert subject.intcode([1,0,0,0,99]) == [2,0,0,0,99]
    assert subject.intcode([2,3,0,3,99]) == [2,3,0,6,99]
    assert subject.intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert subject.intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]
    assert subject.intcode([1002,4,3,4,33]) == [1002,4,3,4,99]
    output = []
    for x in range(7,10):
        input = [x]
        subject.intcode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], input, output)
    assert output == [999, 1000, 1001]


