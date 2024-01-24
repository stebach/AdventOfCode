import solve_2020_06 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'abc',
        '',
        'a',
        'b',
        'c',
        '',
        'ab',
        'ac',
        '',
        'a',
        'a',
        'a',
        'a',
        '',
        'b'
    ]


def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        ('abc',),
        ('a','b','c'),
        ('ab','ac'),
        ('a','a','a','a'),
        ('b',)
    )

def test_unique_answers(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert not set(subject.unique_answers(data[0])) ^ set(['a','b','c'])
    assert not set(subject.unique_answers(data[1])) ^ set(['a','b','c'])
    assert not set(subject.unique_answers(data[2])) ^ set(['a','b','c'])
    assert not set(subject.unique_answers(data[3])) ^ set(['a'])
    assert not set(subject.unique_answers(data[4])) ^ set(['b'])

def test_same_answers(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert not set(subject.same_answers(data[0])) ^ set(['a','b','c'])
    assert not set(subject.same_answers(data[1])) ^ set([])
    assert not set(subject.same_answers(data[2])) ^ set(['a'])
    assert not set(subject.same_answers(data[3])) ^ set(['a'])
    assert not set(subject.same_answers(data[4])) ^ set(['b'])


