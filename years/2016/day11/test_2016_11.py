import solve_2016_11 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.',
        'The second floor contains a hydrogen generator.',
        'The third floor contains a lithium generator.',
        'The fourth floor contains nothing relevant.'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'elevator':0,
        'floors':[
            [['hydrogen','microchip'],['lithium','microchip']],
            [['hydrogen','generator']],
            [['lithium','generator']],
            []
        ]
    }

def test_move_to_top_floor(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.move_to_top_floor(data) == 11



