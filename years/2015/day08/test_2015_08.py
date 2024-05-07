import solve_2015_08 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '""',
        '"abc"',
        '"aaa\\"aaa"',
        '"\\x27"',
    ]

def test_num_memory(puzzle_input):
    assert subject.num_memory(puzzle_input[0]) == 2
    assert subject.num_memory(puzzle_input[1]) == 5
    assert subject.num_memory(puzzle_input[2]) == 10
    assert subject.num_memory(puzzle_input[3]) == 6

def test_num_literal(puzzle_input):
    assert subject.num_literal(puzzle_input[0]) == 0
    assert subject.num_literal(puzzle_input[1]) == 3
    assert subject.num_literal(puzzle_input[2]) == 7
    assert subject.num_literal(puzzle_input[3]) == 1

def test_num_escaped(puzzle_input):
    assert subject.num_escaped(puzzle_input[0]) == 6
    assert subject.num_escaped(puzzle_input[1]) == 9
    assert subject.num_escaped(puzzle_input[2]) == 16
    assert subject.num_escaped(puzzle_input[3]) == 11

def test_solve(puzzle_input):
    assert sum([subject.num_memory(x) - subject.num_literal(x) for x in puzzle_input]) == 12
    assert sum([subject.num_escaped(x) - subject.num_memory(x) for x in puzzle_input]) == 19



