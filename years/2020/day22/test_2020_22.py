import solve_2020_22 as subject
import pytest
from collections import deque

@pytest.fixture
def puzzle_input():
    return [
        "Player 1:",
        "9",
        "2",
        "6",
        "3",
        "1",
        "",
        "Player 2:",
        "5",
        "8",
        "4",
        "7",
        "10"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        deque([9, 2, 6, 3, 1]),
        deque([5, 8, 4, 7, 10])
    )

def test_play(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    subject.play(data)
    assert data == (
        deque([]),
        deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
    )

def test_scoring(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    subject.play(data)
    assert(subject.scoring(data) == 306)

def test_play_recursive(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    subject.play_recursive(data)
    assert data == (
        deque([]),
        deque([7, 5, 6, 2, 4, 1, 10, 8, 9, 3])
    )

