import solve_2021_14 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "NNCB",
        "",
        "CH -> B",
        "HH -> N",
        "CB -> H",
        "NH -> C",
        "HB -> C",
        "HC -> B",
        "HN -> C",
        "NN -> C",
        "BH -> H",
        "NC -> B",
        "NB -> B",
        "BN -> B",
        "BB -> N",
        "BC -> B",
        "CC -> N",
        "CN -> C"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == [
        {
            "NN":1,
            "NC":1,
            "CB":1
        },
        {
            "N":2,
            "C":1,
            "B":1
        },
        {
            "CH": "B",
            "HH": "N",
            "CB": "H",
            "NH": "C",
            "HB": "C",
            "HC": "B",
            "HN": "C",
            "NN": "C",
            "BH": "H",
            "NC": "B",
            "NB": "B",
            "BN": "B",
            "BB": "N",
            "BC": "B",
            "CC": "N",
            "CN": "C"
        }
    ]

def test_steps(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.steps(data, 1)[0:2] == [
        {
            "NC":1,
            "CN":1,
            "NB":1,
            "BC":1,
            "CH":1,
            "HB":1,
        },
        {
            "N":2,
            "C":2,
            "B":2,
            "H":1
        }
    ]
    assert subject.steps(data, 2)[0:2] == [
        {
            "NB":2,
            "BC":2,
            "CC":1,
            "CN":1,
            "BB":2,
            "CB":2,
            "BH":1,
            "HC":1,
        },
        {
            "N":2,
            "C":4,
            "B":6,
            "H":1
        }
    ]

def test_calc_result(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.calc_result(data, 10) == 1588
    assert subject.calc_result(data, 40) == 2188189693529
