import solve_2017_08 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "b inc 5 if a > 1",
        "a inc 1 if b < 5",
        "c dec -10 if a >= 1",
        "c inc -20 if c == 10"
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ("b","inc",5,"a",">",1),
        ("a","inc",1,"b","<",5),
        ("c","dec",-10,"a",">=",1),
        ("c","inc",-20,"c","==",10),
    )

def test_get_max(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_max(data) == 1
    assert subject.get_max(data, True) == 10

