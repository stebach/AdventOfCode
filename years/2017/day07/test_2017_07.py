import solve_2017_07 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "pbga (66)",
        "xhth (57)",
        "ebii (61)",
        "havc (66)",
        "ktlj (57)",
        "fwft (72) -> ktlj, cntj, xhth",
        "qoyq (66)",
        "padx (45) -> pbga, havc, qoyq",
        "tknk (41) -> ugml, padx, fwft",
        "jptl (61)",
        "ugml (68) -> gyxo, ebii, jptl",
        "gyxo (61)",
        "cntj (57)"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        "name": "tknk",
        "weight": 41,
        "sub": [
            {
                "name": "ugml",
                "weight": 68,
                "sub": [
                    {
                        "name": "gyxo",
                        "weight": 61,
                        "sub": []
                    },
                    {
                        "name": "ebii",
                        "weight": 61,
                        "sub": []
                    },
                    {
                        "name": "jptl",
                        "weight": 61,
                        "sub": []
                    }
                ]
            },
            {
                "name": "padx",
                "weight": 45,
                "sub": [
                    {
                        "name": "pbga",
                        "weight": 66,
                        "sub": []
                    },
                    {
                        "name": "havc",
                        "weight": 66,
                        "sub": []
                    },
                    {
                        "name": "qoyq",
                        "weight": 66,
                        "sub": []
                    }
                ]
            },
            {
                "name": "fwft",
                "weight": 72,
                "sub": [
                    {
                        "name": "ktlj",
                        "weight": 57,
                        "sub": []
                    },
                    {
                        "name": "cntj",
                        "weight": 57,
                        "sub": []
                    },
                    {
                        "name": "xhth",
                        "weight": 57,
                        "sub": []
                    }
                ]
            }
        ]
    }

def test_get_root(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert data['name'] == 'tknk'

def test_get_weight_to_balance(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.get_weight_to_balance(data) == 60


