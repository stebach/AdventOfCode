import solve_2022_11 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "Monkey 0:",
        "  Starting items: 79, 98",
        "  Operation: new = old * 19",
        "  Test: divisible by 23",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 3",
        "",
        "Monkey 1:",
        "  Starting items: 54, 65, 75, 74",
        "  Operation: new = old + 6",
        "  Test: divisible by 19",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 0",
        "",
        "Monkey 2:",
        "  Starting items: 79, 60, 97",
        "  Operation: new = old * old",
        "  Test: divisible by 13",
        "    If true: throw to monkey 1",
        "    If false: throw to monkey 3",
        "",
        "Monkey 3:",
        "  Starting items: 74",
        "  Operation: new = old + 3",
        "  Test: divisible by 17",
        "    If true: throw to monkey 0",
        "    If false: throw to monkey 1"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        {
            'items': [79, 98],
            'operation': (1, 19),
            'test': 23,
            'test_true': 2,
            'test_false': 3,
            'inspections': 0
        },
        {
            'items': [54, 65, 75, 74],
            'operation': (2, 6),
            'test': 19,
            'test_true': 2,
            'test_false': 0,
            'inspections': 0
        },
        {
            'items': [79, 60, 97],
            'operation': (1,),
            'test': 13,
            'test_true': 1,
            'test_false': 3,
            'inspections': 0
        },
        {
            'items': [74],
            'operation': (2,3),
            'test': 17,
            'test_true': 0,
            'test_false': 1,
            'inspections': 0
        },
    )

def test_monkey_business_level(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.monkey_business_level(data, 20) == 10_605
    assert subject.monkey_business_level(data, 10_000, False) == 2_713_310_158
