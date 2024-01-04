import solve_2019_07 as subject
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



@pytest.fixture
def puzzle_input():
    return [1, 2, 3]

@pytest.mark.skip(reason="not yet implemented")
def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == [1, 2, 3]

def test_run_amplifiers():
    assert subject.run_amplifiers(4,3,2,1,0, [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]) == 43210
    assert subject.run_amplifiers(0,1,2,3,4, [3,23,3,24,1002,24,10,24,1002,23,-1,23,
101,5,23,23,1,24,23,23,4,23,99,0,0]) == 54321
    assert subject.run_amplifiers(1,0,4,3,2, [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]) == 65210

def test_run_amplifiers_advanced():
    assert subject.run_amplifiers_advanced(9,8,7,6,5, [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]) == 139629729
    assert subject.run_amplifiers_advanced(9,7,8,5,6, [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]) == 18216
