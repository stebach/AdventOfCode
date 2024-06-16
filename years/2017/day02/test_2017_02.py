import solve_2017_02 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ['5	1	9	5',
    '7	5	3',
    '2	4	6	8']

@pytest.fixture
def puzzle_input2():
    return ['5	9	2	8',
    '9	4	7	3',
    '3	8	6	5']

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (5,1,9,5),
        (7,5,3),
        (2,4,6,8),
    )

def test_checksum(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.checksum(data) == 18

def test_checksum2(puzzle_input2):
    data = tuple(map(subject.parse_line, puzzle_input2))
    assert subject.checksum2(data) == 9

