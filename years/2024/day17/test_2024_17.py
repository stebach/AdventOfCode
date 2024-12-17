import solve_2024_17 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'Register A: 729',
        'Register B: 0',
        'Register C: 0',
        '',
        'Program: 0,1,5,4,3,0'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        'Register A: 2024',
        'Register B: 0',
        'Register C: 0',
        'Program: 0,3,5,4,3,0'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'registers': {'A': 729, 'B': 0, 'C': 0},
        'program': [0, 1, 5, 4, 3, 0]
    }

def test_get_output(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.get_output(data) == [4,6,3,5,6,3,5,2,1,0]



