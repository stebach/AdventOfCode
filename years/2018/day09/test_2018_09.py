import solve_2018_09 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return "10 players; last marble is worth 1618 points"

def test_parse_line(puzzle_input):
    assert subject.parse_line(puzzle_input) == (10, 1618)
    assert subject.parse_line("13 players; last marble is worth 7999 points") == (13, 7999)
    assert subject.parse_line("17 players; last marble is worth 1104 points") == (17, 1104)

def test_part1_example1():
    assert subject.part1((10, 1618)) == 8317
    assert subject.part1((13, 7999)) == 146373
    assert subject.part1((17, 1104)) == 2764
    assert subject.part1((21, 6111)) == 54718
    assert subject.part1((30, 5807)) == 37305


