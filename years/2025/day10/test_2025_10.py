import solve_2025_10 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}',
        '[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}',
        '[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (0b0110, (0b0001, 0b0101, 0b0010, 0b0011, 0b1010, 0b1100), [3, 5, 4, 7]),
        (0b00010, (0b10111, 0b00110, 0b10001, 0b11100, 0b01111), [7, 5, 12, 7, 2]),
        (0b011101, (0b111110, 0b100110, 0b111011, 0b011000), [10, 11, 11, 5, 10, 5])
    )

def test_get_fewest_buttons(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_fewest_buttons(data[0]) == 2
    assert subject.get_fewest_buttons(data[1]) == 3
    assert subject.get_fewest_buttons(data[2]) == 2

def test_get_fewest_buttons_for_joltage(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_fewest_buttons_for_joltage(data[0]) == 10
    assert subject.get_fewest_buttons_for_joltage(data[1]) == 12
    assert subject.get_fewest_buttons_for_joltage(data[2]) == 11

def test_solve(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.solve(data) == (7,33)

