import solve_2021_03 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        4,
        30,
        22,
        23,
        0b10101,
        0b01111,
        0b00111,
        0b11100,
        0b10000,
        0b11001,
        0b00010,
        0b01010
    )

def test_get_power_consumption(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_power_consumption(data) == 198

def test_get_oxygen_generator_rating(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_oxygen_generator_rating(data) == 230


