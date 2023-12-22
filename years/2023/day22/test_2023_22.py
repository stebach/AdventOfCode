import solve_2023_22 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '1,0,1~1,2,1',
        '0,0,2~2,0,2',
        '0,2,3~2,2,3',
        '0,0,4~0,2,4',
        '2,0,5~2,2,5',
        '0,1,6~2,1,6',
        '1,1,8~1,1,9'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ([1,0,1],[1,2,1]),
        ([2,0,0],[2,0,2]),
        ([3,2,0],[3,2,2]),
        ([4,0,0],[4,2,0]),
        ([5,0,2],[5,2,2]),
        ([6,1,0],[6,1,2]),
        ([8,1,1],[9,1,1])
    )

def test_part1_example1(puzzle_input):
    assert subject.part1(tuple(map(subject.parse_line, puzzle_input))) == 5

def test_part2_example1(puzzle_input):
    assert subject.part2(tuple(map(subject.parse_line, puzzle_input))) == 7

