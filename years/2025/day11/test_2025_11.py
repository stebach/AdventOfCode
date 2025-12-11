import solve_2025_11 as subject
import pytest
import collections

@pytest.fixture
def puzzle_input():
    return [
        'aaa: you hhh',
        'you: bbb ccc',
        'bbb: ddd eee',
        'ccc: ddd eee fff',
        'ddd: ggg',
        'eee: out',
        'fff: out',
        'ggg: out',
        'hhh: ccc fff iii',
        'iii: out'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        'svr: aaa bbb',
        'aaa: fft',
        'fft: ccc',
        'bbb: tty',
        'tty: ccc',
        'ccc: ddd eee',
        'ddd: hub',
        'hub: fff',
        'eee: dac',
        'dac: fff',
        'fff: ggg hhh',
        'ggg: out',
        'hhh: out',
    ]

def test_parse_lines(puzzle_input):
    Path = collections.namedtuple('Path', ['source', 'targets'])
    assert subject.parse_lines(puzzle_input) == (
        Path('aaa',('you', 'hhh')),
        Path('you',('bbb', 'ccc')),
        Path('bbb',('ddd', 'eee')),
        Path('ccc',('ddd', 'eee', 'fff')),
        Path('ddd',('ggg',)),
        Path('eee',('out',)),
        Path('fff',('out',)),
        Path('ggg',('out',)),
        Path('hhh',('ccc', 'fff', 'iii')),
        Path('iii',('out',))
    )

def test_count_all_paths(puzzle_input, puzzle_input2):
    data = subject.parse_lines(puzzle_input)
    assert subject.count_all_paths(data, 'you', 'out') == 5
    data2 = subject.parse_lines(puzzle_input2)
    assert subject.count_all_paths(data2, 'svr', 'out', ('dac','fft')) == 2

