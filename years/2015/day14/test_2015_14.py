import solve_2015_14 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
        'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('Comet', 14, 10, 127),
        ('Dancer', 16, 11, 162)
    )

def test_get_distance(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_distance(data[0], 1000) == 1120
    assert subject.get_distance(data[1], 1000) == 1056

def test_get_scores(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_scores(data, 1000) == [312, 689]
