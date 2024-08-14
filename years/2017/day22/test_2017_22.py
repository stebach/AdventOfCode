import solve_2017_22 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ['..#','#..','...']

def test_parse_line(puzzle_input):
    assert list(map(subject.parse_line, puzzle_input)) == [['.','.','#'],['#','.','.'],['.','.','.']]

def test_count_burst_infections(puzzle_input):
    data = list(map(subject.parse_line, puzzle_input))
    assert subject.count_burst_infections(data) == 5587
    assert subject.count_burst_infections(data, 100, 4, 0, 2, 3) == 26
    assert subject.count_burst_infections(data, 10_000_000, 4, 0, 2, 3) == 2_511_944

