import solve_2018_17 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'x=495, y=2..7',
        'y=7, x=495..501',
        'x=501, y=3..7',
        'x=498, y=2..4',
        'x=506, y=1..2',
        'x=498, y=10..13',
        'x=504, y=10..13',
        'y=13, x=498..504'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        (495,2),
        (495,3),
        (495,4),
        (495,5),
        (495,6),
        (495,7),
        (496,7),
        (497,7),
        (498,7),
        (499,7),
        (500,7),
        (501,7),
        (501,3),
        (501,4),
        (501,5),
        (501,6),
        (498,2),
        (498,3),
        (498,4),
        (506,1),
        (506,2),
        (498,10),
        (498,11),
        (498,12),
        (498,13),
        (504,10),
        (504,11),
        (504,12),
        (504,13),
        (499,13),
        (500,13),
        (501,13),
        (502,13),
        (503,13),
    )

def test_part1_example1(puzzle_input):
    assert subject.part1(subject.parse_lines(puzzle_input)) == 57

def test_part2_example1(puzzle_input):
    assert subject.part2(subject.parse_lines(puzzle_input)) == 29
