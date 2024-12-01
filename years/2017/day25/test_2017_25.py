import solve_2017_25 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'Begin in state A.',
        'Perform a diagnostic checksum after 6 steps.',
        '',
        'In state A:',
        '  If the current value is 0:',
        '    - Write the value 1.',
        '    - Move one slot to the right.',
        '    - Continue with state B.',
        '  If the current value is 1:',
        '    - Write the value 0.',
        '    - Move one slot to the left.',
        '    - Continue with state B.',
        '',
        'In state B:',
        '  If the current value is 0:',
        '    - Write the value 1.',
        '    - Move one slot to the left.',
        '    - Continue with state A.',
        '  If the current value is 1:',
        '    - Write the value 1.',
        '    - Move one slot to the right.',
        '    - Continue with state A.'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'begin': 'A',
        'checksum_after': 6,
        'states': {
            'A': {
                0: [1, 1, 'B'],
                1: [0, -1, 'B']
            },
            'B': {
                0: [1, -1, 'A'],
                1: [1, 1, 'A']
            },
        }
    }

def test_get_checksum(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.get_checksum(data) == 3

