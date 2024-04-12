import solve_2021_23 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "#############",
        "#...........#",
        "###B#C#B#D###",
        "  #A#D#C#A#",
        "  #########"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        [[2,2],[8,2]],
        [[2,1],[6,1]],
        [[4,1],[6,2]],
        [[8,1],[4,2]],
    )

def test_least_energy(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.least_energy(data) == 12521
    data = subject.modify_input(subject.parse_lines(puzzle_input))
    assert subject.least_energy(data) == 44169

def test_modify_input(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.modify_input(data) == (
        [[2,4],[8,4],[8,2],[6,3]],
        [[2,1],[6,1],[6,2],[4,3]],
        [[4,1],[6,4],[4,2],[8,3]],
        [[8,1],[4,4],[2,2],[2,3]],
    )
