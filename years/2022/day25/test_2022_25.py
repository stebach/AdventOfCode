import solve_2022_25 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "1=-0-2",
        "12111",
        "2=0=",
        "21",
        "2=01",
        "111",
        "20012",
        "112",
        "1=-1=",
        "1-12",
        "12",
        "1=",
        "122"
    ]

def test_snafu(puzzle_input):
    assert subject.snafu("1") == 1
    assert subject.snafu("2") == 2
    assert subject.snafu("1=") == 3
    assert subject.snafu("1-") == 4
    assert subject.snafu("10") == 5
    assert subject.snafu("11") == 6
    assert subject.snafu("12") == 7
    assert subject.snafu("2=") == 8
    assert subject.snafu("2-") == 9
    assert subject.snafu("20") == 10
    assert subject.snafu("1=0") == 15
    assert subject.snafu("1-0") == 20
    assert subject.snafu("1=11-2") == 2022
    assert subject.snafu("1-0---0") == 12345
    assert subject.snafu("1121-1110-1=0") == 314159265
    assert sum([subject.snafu(x) for x in puzzle_input]) == 4890

def test_to_snafu():
    assert subject.to_snafu(1) == "1"
    assert subject.to_snafu(2) == "2"
    assert subject.to_snafu(3) == "1="
    assert subject.to_snafu(4) == "1-"
    assert subject.to_snafu(5) == "10"
    assert subject.to_snafu(6) == "11"
    assert subject.to_snafu(7) == "12"
    assert subject.to_snafu(8) == "2="
    assert subject.to_snafu(9) == "2-"
    assert subject.to_snafu(10) == "20"
    assert subject.to_snafu(15) == "1=0"
    assert subject.to_snafu(20) == "1-0"
    assert subject.to_snafu(2022) == "1=11-2"
    assert subject.to_snafu(12345) == "1-0---0"
    assert subject.to_snafu(314159265) == "1121-1110-1=0"
