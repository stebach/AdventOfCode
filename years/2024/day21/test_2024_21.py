import solve_2024_21 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '029A',
        '980A',
        '179A',
        '456A',
        '379A',
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('0', '2', '9', 'A'),
        ('9', '8', '0', 'A'),
        ('1', '7', '9', 'A'),
        ('4', '5', '6', 'A'),
        ('3', '7', '9', 'A'),
    )

def test_get_complexity(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_complexity(data[0]) == 68 * 29
    assert subject.get_complexity(data[1]) == 60 * 980
    assert subject.get_complexity(data[2]) == 68 * 179
    assert subject.get_complexity(data[3]) == 64 * 456
    assert subject.get_complexity(data[4]) == 64 * 379
    assert sum([subject.get_complexity(x) for x in data]) == 126384

def test_solve(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.solve(data) == (126384, 154115708116294)

