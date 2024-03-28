import solve_2021_09 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678"
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        [2,1,9,9,9,4,3,2,1,0],
        [3,9,8,7,8,9,4,9,2,1],
        [9,8,5,6,7,8,9,8,9,2],
        [8,7,6,7,8,9,6,7,8,9],
        [9,8,9,9,9,6,5,6,7,8]
    )

def test_find_low_point_risk_level(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.find_low_point_risk_level(data) == 15

def test_find_basins(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.find_basins(data) == {
        'grid': [
            [-1,-1,9,9,9,-2,-2,-2,-2,-2],
            [-1,9,-3,-3,-3,9,-2,9,-2,-2],
            [9,-3,-3,-3,-3,-3,9,-5,9,-2],
            [-3,-3,-3,-3,-3,9,-5,-5,-5,9],
            [9,-3,9,9,9,-5,-5,-5,-5,-5]
        ],
        'count': {
            -1: 3,
            -2: 9,
            -3: 14,
            -5: 9
        },
        'areas_by_size': [14, 9, 9, 3]
    }

