import solve_2015_22 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'Hit Points: 13',
        'Damage: 8'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'hitpoints': 13,
        'damage': 8
    }

def test_least_mana_used(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.least_mana_used(data, 10, 250) == 226
    data['hitpoints'] = 14
    assert subject.least_mana_used(data, 10, 250) == 641