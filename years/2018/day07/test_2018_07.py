import solve_2018_07 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "Step C must be finished before step A can begin.",
        "Step C must be finished before step F can begin.",
        "Step A must be finished before step B can begin.",
        "Step A must be finished before step D can begin.",
        "Step B must be finished before step E can begin.",
        "Step D must be finished before step E can begin.",
        "Step F must be finished before step E can begin."
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        "A": ["C"],
        "F": ["C"],
        "B": ["A"],
        "D": ["A"],
        "E": ["B","D","F"]
    }

def test_part1_example1(puzzle_input):
    assert subject.part1(subject.parse_lines(puzzle_input)) == "CABDFE"

def test_part2_example1(puzzle_input):
    assert subject.part2(subject.parse_lines(puzzle_input), 2, 0) == 15

