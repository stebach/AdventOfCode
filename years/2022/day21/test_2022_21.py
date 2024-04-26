import solve_2022_21 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "root: pppw + sjmn",
        "dbpl: 5",
        "cczh: sllz + lgvd",
        "zczc: 2",
        "ptdq: humn - dvpt",
        "dvpt: 3",
        "lfqf: 4",
        "humn: 5",
        "ljgn: 2",
        "sjmn: drzm * dbpl",
        "sllz: 4",
        "pppw: cczh / lfqf",
        "lgvd: ljgn * ptdq",
        "drzm: hmdt - zczc",
        "hmdt: 32"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'root': {
            'type': '+',
            'attr': ['pppw','sjmn'],
        },
        'dbpl': {
            'type': 'num',
            'attr': 5,
        },
        'cczh': {
            'type': '+',
            'attr': ['sllz','lgvd'],
        },
        'zczc': {
            'type': 'num',
            'attr': 2,
        },
        'ptdq': {
            'type': '-',
            'attr': ['humn','dvpt'],
        },
        'dvpt': {
            'type': 'num',
            'attr': 3,
        },
        'lfqf': {
            'type': 'num',
            'attr': 4,
        },
        'humn': {
            'type': 'num',
            'attr': 5,
        },
        'ljgn': {
            'type': 'num',
            'attr': 2,
        },
        'sjmn': {
            'type': '*',
            'attr': ['drzm','dbpl'],
        },
        'sllz': {
            'type': 'num',
            'attr': 4,
        },
        'pppw': {
            'type': '/',
            'attr': ['cczh', 'lfqf'],
        },
        'lgvd': {
            'type': '*',
            'attr': ['ljgn','ptdq'],
        },
        'drzm': {
            'type': '-',
            'attr': ['hmdt','zczc'],
        },
        'hmdt': {
            'type': 'num',
            'attr': 32
        },
    }

def test_get_monkey_roll(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.get_monkey_roll(data) == 152

def test_get_number_to_pass_equality_test(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.get_number_to_pass_equality_test(data) == 301

