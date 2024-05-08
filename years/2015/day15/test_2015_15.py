import solve_2015_15 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
        'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
    ]

def test_parse_line(puzzle_input):
    assert dict(map(subject.parse_line, puzzle_input)) == {
        'Butterscotch': {
            'capacity': -1,
            'durability': -2,
            'flavor': 6,
            'texture': 3,
            'calories': 8
        },
        'Cinnamon': {
            'capacity': 2,
            'durability': 3,
            'flavor': -2,
            'texture': -1,
            'calories': 3
        }
    }

def test_get_high_score(puzzle_input):
    data = dict(map(subject.parse_line, puzzle_input))
    assert subject.get_high_score(data) == 62842880
    assert subject.get_high_score(data, 500) == 57600000
