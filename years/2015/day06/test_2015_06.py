import solve_2015_06 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'turn on 0,0 through 999,999',
        'toggle 0,0 through 999,0',
        'turn off 499,499 through 500,500',
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('on', 0, 0, 999, 999),
        ('toggle', 0, 0, 999, 0),
        ('off', 499, 499, 500, 500),
    )

def test_count_lights(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.count_lights(data) == 998996

def test_total_brightness(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.total_brightness(data) == 1_001_996

