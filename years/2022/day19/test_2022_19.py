import solve_2022_19 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.",
        "Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (1, 4, 2, 3, 14, 2, 7),
        (2, 2, 3, 3, 8, 3, 12),
    )

def test_get_quality_level(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_quality_level(data) == 33

def test_get_geodes_of_first_blueprints(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_geodes_of_first_blueprints(data, 3) == 3472


