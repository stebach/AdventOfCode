import solve_2021_21 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "Player 1 starting position: 4",
        "Player 2 starting position: 8"
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (4,8)

def test_play_deterministic(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.play_deterministic(data) == 739_785

def test_play_dirac(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.play_dirac(data) == 444_356_092_776_315

