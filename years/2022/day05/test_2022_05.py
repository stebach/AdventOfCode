import solve_2022_05 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ["    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3 ",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2"]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        [
            ['Z','N'],
            ['M','C','D'],
            ['P']
        ],
        (
            (1,1,0),
            (3,0,2),
            (2,1,0),
            (1,0,1),
        )
    )

def test_move(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.move(data) == 'CMZ'

    assert subject.move(data, True) == 'MCD'


