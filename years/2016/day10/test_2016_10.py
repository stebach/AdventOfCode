import solve_2016_10 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'value 5 goes to bot 2',
        'bot 2 gives low to bot 1 and high to bot 0',
        'value 3 goes to bot 1',
        'bot 1 gives low to output 1 and high to bot 0',
        'bot 0 gives low to output 2 and high to output 0',
        'value 2 goes to bot 2'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        {
            'has':[],
            'gives':[['output',2],['output',0]],
        },
        {
            'has':[3],
            'gives':[['output',1],['bot',0]],
        },
        {
            'has':[5,2],
            'gives':[['bot',1],['bot',0]],
        },
    )

def test_find_responsible(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.find_responsible(data, (2,5)) == 2


