import solve_2022_03 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        [[22,36,18,23,16,49,20,23,36,7,49,18,],[8,3,19,32,39,39,6,32,32,8,32,16,]],
        [[10,17,34,44,40,17,44,10,17,26,10,33,30,38,33,38,],[18,19,32,39,6,32,52,45,18,38,18,32,52,19,45,38,]],
        [[42,13,13,4,26,17,42,18,48,],[22,42,23,23,46,49,28,23,7,]],
        [[23,39,17,22,38,39,52,34,8,34,39,22,23,38,34,],[10,2,22,3,10,14,14,45,28,14,22,46,43,32,14,]],
        [[20,20,7,36,20,44,33,36,],[43,3,20,46,52,20,52,46,]],
        [[29,18,52,19,36,19,42,42,52,19,33,26,],[23,23,19,38,23,38,13,16,23,39,30,23,]]
    )

def test_double_item_priority(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.double_item_priority(data) == 157

def test_badge_priority(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.badge_priority(data) == 70

