import solve_2019_16 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return '12345678'

@pytest.fixture
def puzzle_input2():
    return '80871224585914546619083218645595'
@pytest.fixture

def puzzle_input3():
    return '19617804207202209144916044189917'

@pytest.fixture
def puzzle_input4():
    return '69317163492948606335995924319873'

@pytest.fixture
def puzzle_input5():
    return '03036732577212944063491565474664'

@pytest.fixture
def puzzle_input6():
    return '02935109699940807407585447034323'

@pytest.fixture
def puzzle_input7():
    return '03081770884921959731165446850517'

def test_get_pattern():
    #0, 1, 0, -1
    assert subject.get_pattern(0) == [0,1,0,-1]
    assert subject.get_pattern(1) == [0,0,1,1,0,0,-1,-1]
    assert subject.get_pattern(2) == [0,0,0,1,1,1,0,0,0,-1,-1,-1]

def test_run_phase(puzzle_input):
    assert subject.run_phase(puzzle_input) == '48226158'

def test_run_phases(puzzle_input, puzzle_input2, puzzle_input3, puzzle_input4):
    assert subject.run_phases(puzzle_input, 1) == '48226158'
    assert subject.run_phases(puzzle_input, 2) == '34040438'
    assert subject.run_phases(puzzle_input, 3) == '03415518'
    assert subject.run_phases(puzzle_input, 4) == '01029498'

    assert subject.run_phases(puzzle_input2, 100)[0:8] == '24176176'
    assert subject.run_phases(puzzle_input3, 100)[0:8] == '73745418'
    assert subject.run_phases(puzzle_input4, 100)[0:8] == '52432133'

def test_real_signal(puzzle_input5, puzzle_input6, puzzle_input7):
    assert subject.real_signal(puzzle_input5) == '84462026'
    assert subject.real_signal(puzzle_input6) == '78725270'
    assert subject.real_signal(puzzle_input7) == '53553731'
