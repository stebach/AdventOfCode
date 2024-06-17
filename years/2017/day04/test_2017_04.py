import solve_2017_04 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "aa bb cc dd ee",
        "aa bb cc dd aa",
        "aa bb cc dd aaa",
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ("aa","bb","cc","dd","ee"),
        ("aa","bb","cc","dd","aa"),
        ("aa","bb","cc","dd","aaa")
    )


def test_check_no_dubles(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.check_no_dubles(data[0]) == True
    assert subject.check_no_dubles(data[1]) == False
    assert subject.check_no_dubles(data[2]) == True

    assert subject.check_no_dubles(("abcde", "fghij"), True) == True
    assert subject.check_no_dubles(("abcde","xyz","ecdab"), True) == False
    assert subject.check_no_dubles(("a","ab","abc","abd","abf","abj"), True) == True
    assert subject.check_no_dubles(("iiii","oiii","ooii","oooi","oooo"), True) == True
    assert subject.check_no_dubles(("oiii","ioii","iioi","iiio"), True) == False

