import solve_2015_09 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'London to Dublin = 464',
        'London to Belfast = 518',
        'Dublin to Belfast = 141'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'London': {
            'Dublin': 464,
            'Belfast': 518,
        },
        'Dublin': {
            'London': 464,
            'Belfast': 141,
        },
        'Belfast': {
            'London': 518,
            'Dublin': 141,
        }
    }

def test_find_shortest(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.find_shortest(data) == 605
    assert subject.find_shortest(data, True) == 982
