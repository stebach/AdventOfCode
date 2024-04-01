import solve_2021_17 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ['target area: x=20..30, y=-10..-5']

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (20,30,-10,-5)

def test_find_highest_y(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.find_highest_y(data) == 45

def test_find_initial_velocity_count(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.find_initial_velocity_count(data) == 112


