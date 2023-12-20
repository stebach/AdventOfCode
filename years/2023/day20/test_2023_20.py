import solve_2023_20 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'broadcaster -> a, b, c',
        '%a -> b',
        '%b -> c',
        '%c -> inv',
        '&inv -> a'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        'broadcaster -> a',
        '%a -> inv, con',
        '&inv -> b',
        '%b -> con',
        '&con -> output'
    ]

def test_parse_lines(puzzle_input, puzzle_input2):
    assert subject.parse_lines(puzzle_input) == {
        'broadcaster': (None, ('a','b','c'), {}),
        'a': ('%', ('b',), { 'global': False }),
        'b': ('%', ('c',), { 'global': False }),
        'c': ('%', ('inv',), { 'global': False }),
        'inv': ('&', ('a',), { 'c': False }),
    }
    assert subject.parse_lines(puzzle_input2) == {
        'broadcaster': (None, ('a',), {}),
        'a': ('%', ('inv', 'con'), { 'global': False }),
        'inv': ('&', ('b',), { 'a': False }),
        'b': ('%', ('con',), { 'global': False }),
        'con': ('&', ('output',), { 'a': False, 'b': False }),
        'output': (None, tuple(), { 'global': True })
    }

def test_part1_example1(puzzle_input):
    assert subject.part1(subject.parse_lines(puzzle_input)) == 32_000_000

def test_part1_example2(puzzle_input2):
    assert subject.part1(subject.parse_lines(puzzle_input2)) == 11_687_500
