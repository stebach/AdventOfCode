import solve_2015_21 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'Hit Points: 12',
        'Damage: 7',
        'Armor: 2'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'hitpoints': 12,
        'damage': 7,
        'armor': 2
    }

def test_fight(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.fight({
        'hitpoints': 8,
        'damage': 5,
        'armor': 5
    }, data) == [2, 0]


