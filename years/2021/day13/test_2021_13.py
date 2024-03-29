import solve_2021_13 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "6,10",
        "0,14",
        "9,10",
        "0,3",
        "10,4",
        "4,11",
        "6,0",
        "6,12",
        "4,1",
        "0,13",
        "10,12",
        "3,4",
        "3,0",
        "8,4",
        "1,10",
        "2,14",
        "8,10",
        "9,0",
        "",
        "fold along y=7",
        "fold along x=5"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == [
        [
            [6,10],
            [0,14],
            [9,10],
            [0,3],
            [10,4],
            [4,11],
            [6,0],
            [6,12],
            [4,1],
            [0,13],
            [10,12],
            [3,4],
            [3,0],
            [8,4],
            [1,10],
            [2,14],
            [8,10],
            [9,0],
        ],
        [
            ['y',7],
            ['x',5]
        ]
    ]

def test_fold(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    subject.fold(data)
    assert data == [
        [
            [6,4],
            [0,0],
            [9,4],
            [0,3],
            [10,4],
            [4,3],
            [6,0],
            [6,2],
            [4,1],
            [0,1],
            [10,2],
            [3,4],
            [3,0],
            [8,4],
            [1,4],
            [2,0],
            [9,0],
        ],
        [
            ['x',5]
        ]
    ] 
    subject.fold(data)
    assert data == [
        [
            [4,4],
            [0,0],
            [1,4],
            [0,3],
            [0,4],
            [4,3],
            [4,0],
            [4,2],
            [4,1],
            [0,1],
            [0,2],
            [3,4],
            [3,0],
            [2,4],
            [2,0],
            [1,0],
        ],
        [
        ]
    ] 

