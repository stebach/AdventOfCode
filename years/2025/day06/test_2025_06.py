import solve_2025_06 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ['123 328  51 64 ', ' 45 64  387 23 ', '  6 98  215 314', '*   +   *   +  ']

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        {
            'numbers': {
                'part1': [123, 45, 6],
                'part2': [1, 24, 356]
            },
            'operation': '*'
        },
        {
            'numbers': {
                'part1': [328, 64, 98],
                'part2': [369, 248, 8]
            },
            'operation': '+'
        },
        {
            'numbers': {
                'part1': [51, 387, 215],
                'part2': [32, 581, 175]
            },
            'operation': '*'
        },
        {
            'numbers': {
                'part1': [64, 23, 314],
                'part2': [623, 431, 4]
            },
            'operation': '+'
        }
    )

def test_solve(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.solve(data) == (4277556, 3263827)

