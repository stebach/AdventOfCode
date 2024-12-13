import solve_2024_13 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'Button A: X+94, Y+34',
        'Button B: X+22, Y+67',
        'Prize: X=8400, Y=5400',
        '',
        'Button A: X+26, Y+66',
        'Button B: X+67, Y+21',
        'Prize: X=12748, Y=12176',
        '',
        'Button A: X+17, Y+86',
        'Button B: X+84, Y+37',
        'Prize: X=7870, Y=6450',
        '',
        'Button A: X+69, Y+23',
        'Button B: X+27, Y+71',
        'Prize: X=18641, Y=10279'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        {
            'A': {'X': 94, 'Y': 34},
            'B': {'X': 22, 'Y': 67},
            'Prize': {'X': 8400, 'Y': 5400}
        },
        {
            'A': {'X': 26, 'Y': 66},
            'B': {'X': 67, 'Y': 21},
            'Prize': {'X': 12748, 'Y': 12176}
        },
        {
            'A': {'X': 17, 'Y': 86},
            'B': {'X': 84, 'Y': 37},
            'Prize': {'X': 7870, 'Y': 6450}
        },
        {
            'A': {'X': 69, 'Y': 23},
            'B': {'X': 27, 'Y': 71},
            'Prize': {'X': 18641, 'Y': 10279}
        }
    )

def test_cheepest(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.cheepest(data[0], 3, 1) == 280
    assert subject.cheepest(data[1], 3, 1) == 0
    assert subject.cheepest(data[2], 3, 1) == 200
    assert subject.cheepest(data[3], 3, 1) == 0

    assert subject.cheepest(data[0], 3, 1, True) == 0
    assert subject.cheepest(data[1], 3, 1, True) == 459236326669
    assert subject.cheepest(data[2], 3, 1, True) == 0
    assert subject.cheepest(data[3], 3, 1, True) == 416082282239

def test_solve(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.solve(data) == (480, 875318608908)

