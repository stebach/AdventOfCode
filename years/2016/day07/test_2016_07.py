import solve_2016_07 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return (
        'abba[mnop]qrst',
        'abcd[bddb]xyyx',
        'aaaa[qwer]tyui',
        'ioxxoj[asdfgh]zxcvbn',
        'aba[bab]xyz',
        'xyx[xyx]xyx',
        'aaa[kek]eke',
        'zazbz[bzb]cdb'
    )

def test_abba_outside_brackets(puzzle_input):
    assert subject.abba_outside_brackets(puzzle_input[0]) == True
    assert subject.abba_outside_brackets(puzzle_input[1]) == True
    assert subject.abba_outside_brackets(puzzle_input[2]) == False
    assert subject.abba_outside_brackets(puzzle_input[3]) == True

def test_abba_inside_brackets(puzzle_input):
    assert subject.abba_inside_brackets(puzzle_input[0]) == False
    assert subject.abba_inside_brackets(puzzle_input[1]) == True
    assert subject.abba_inside_brackets(puzzle_input[2]) == False
    assert subject.abba_inside_brackets(puzzle_input[3]) == False

def test_supports_tls(puzzle_input):
    assert subject.supports_tls(puzzle_input[0]) == True
    assert subject.supports_tls(puzzle_input[1]) == False
    assert subject.supports_tls(puzzle_input[2]) == False
    assert subject.supports_tls(puzzle_input[3]) == True


def test_supports_ssl(puzzle_input):
    assert subject.supports_ssl(puzzle_input[4]) == True
    assert subject.supports_ssl(puzzle_input[5]) == False
    assert subject.supports_ssl(puzzle_input[6]) == True
    assert subject.supports_ssl(puzzle_input[7]) == True

