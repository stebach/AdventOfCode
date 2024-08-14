import solve_2017_21 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '../.# => ##./#../...',
        '.#./..#/### => #..#/..../..../#..#'
    ]

def test_parse_line(puzzle_input):
    assert dict(map(subject.parse_line, puzzle_input)) == {
        '../.#': ('##.','#..','...'),
        '.#./..#/###': ('#..#','....','....','#..#'),
    }

def test_count_on(puzzle_input):
    data = dict(map(subject.parse_line, puzzle_input))
    assert subject.count_on(data, 2) == 12


