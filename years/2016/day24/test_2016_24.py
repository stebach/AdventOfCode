import solve_2016_24 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '###########',
        '#0.1.....2#',
        '#.#######.#',
        '#4.......3#',
        '###########'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        {0: (1,1), 1: (3,1), 2: (9,1), 4: (1,3), 3: (9,3)},
        (
            (1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),
            (1,2),(9,2),
            (1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(8,3),(9,3),
        )
    )

def test_collect_all(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.collect_all(data) == 14

