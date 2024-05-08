import solve_2015_13 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'Alice would gain 54 happiness units by sitting next to Bob.',
        'Alice would lose 79 happiness units by sitting next to Carol.',
        'Alice would lose 2 happiness units by sitting next to David.',
        'Bob would gain 83 happiness units by sitting next to Alice.',
        'Bob would lose 7 happiness units by sitting next to Carol.',
        'Bob would lose 63 happiness units by sitting next to David.',
        'Carol would lose 62 happiness units by sitting next to Alice.',
        'Carol would gain 60 happiness units by sitting next to Bob.',
        'Carol would gain 55 happiness units by sitting next to David.',
        'David would gain 46 happiness units by sitting next to Alice.',
        'David would lose 7 happiness units by sitting next to Bob.',
        'David would gain 41 happiness units by sitting next to Carol.'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'Alice': {
            'Bob': 54,
            'Carol': -79,
            'David': -2,
        },
        'Bob': {
            'Alice': 83,
            'Carol': -7,
            'David': -63,
        },
        'Carol': {
            'Alice': -62,
            'Bob': 60,
            'David': 55,
        },
        'David': {
            'Alice': 46,
            'Bob': -7,
            'Carol': 41,
        }
    }

def test_find_optimal_seating(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.find_optimal_seating(data) == 330
