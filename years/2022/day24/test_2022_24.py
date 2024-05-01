import solve_2022_24 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '#.######',
        '#>>.<^<#',
        '#.<..<<#',
        '#>v.><>#',
        '#<^v^^>#',
        '######.#'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'blizzards': (
            ([1,1], (1,0)),
            ([2,1], (1,0)),
            ([4,1], (-1,0)),
            ([5,1], (0,-1)),
            ([6,1], (-1,0)),
            ([2,2], (-1,0)),
            ([5,2], (-1,0)),
            ([6,2], (-1,0)),
            ([1,3], (1,0)),
            ([2,3], (0,1)),
            ([4,3], (1,0)),
            ([5,3], (-1,0)),
            ([6,3], (1,0)),
            ([1,4], (-1,0)),
            ([2,4], (0,-1)),
            ([3,4], (0,1)),
            ([4,4], (0,-1)),
            ([5,4], (0,-1)),
            ([6,4], (1,0)),
        ),
        'bounds': (7,5),
        'start': (1,0),
        'end': (6,5),
        'to_start': (1,1),
        'to_end': (6,4)
    }

def test_get_minutes(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.get_minutes(data) == 18
    assert subject.get_minutes(data, True) == 54
    

