import solve_2024_01 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '3   4',
        '4   3',
        '2   5',
        '1   3',
        '3   9',
        '3   3'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == [
        [3,4,2,1,3,3],
        [4,3,5,3,9,3],
    ]

def test_get_distances_ordered(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.get_distances_ordered(data) == 11

def test_get_similarity_score(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.get_similarity_score(data) == 31

def test_solve(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.solve(data) == (11,31)

