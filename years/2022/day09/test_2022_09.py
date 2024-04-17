import solve_2022_09 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'R 4',
        'U 4',
        'L 3',
        'D 1',
        'R 4',
        'D 1',
        'L 5',
        'R 2'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        'R 5',
        'U 8',
        'L 8',
        'D 3',
        'R 17',
        'D 10',
        'L 25',
        'U 20'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('R', 4),
        ('U', 4),
        ('L', 3),
        ('D', 1),
        ('R', 4),
        ('D', 1),
        ('L', 5),
        ('R', 2)
    )

def test_count_tail_pos(puzzle_input, puzzle_input2):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.count_tail_pos(data) == 13
    assert subject.count_tail_pos(data, 10) == 1

    data = tuple(map(subject.parse_line, puzzle_input2))
    assert subject.count_tail_pos(data, 10) == 36

