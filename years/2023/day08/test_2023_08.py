import solve_2023_08 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "RL",
        "",
        "AAA = (BBB, CCC)",
        "BBB = (DDD, EEE)",
        "CCC = (ZZZ, GGG)",
        "DDD = (DDD, DDD)",
        "EEE = (EEE, EEE)",
        "GGG = (GGG, GGG)",
        "ZZZ = (ZZZ, ZZZ)"
    ]

@pytest.fixture
def puzzle_input2():
    return [
        "LLR",
        "",
        "AAA = (BBB, BBB)",
        "BBB = (AAA, ZZZ)",
        "ZZZ = (ZZZ, ZZZ)"
    ]

@pytest.fixture
def puzzle_input3():
    return [
        "LR",
        "",
        "11A = (11B, XXX)",
        "11B = (XXX, 11Z)",
        "11Z = (11B, XXX)",
        "22A = (22B, XXX)",
        "22B = (22C, 22C)",
        "22C = (22Z, 22Z)",
        "22Z = (22B, 22B)",
        "XXX = (XXX, XXX)"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == tuple([
        [1, 0],
        {
            'AAA': ['BBB', 'CCC'],
            'BBB': ['DDD', 'EEE'],
            'CCC': ['ZZZ', 'GGG'],
            'DDD': ['DDD', 'DDD'],
            'EEE': ['EEE', 'EEE'],
            'GGG': ['GGG', 'GGG'],
            'ZZZ': ['ZZZ', 'ZZZ']
        }
    ])

def test_part1_example1(puzzle_input, puzzle_input2):
    data = subject.parse_lines(puzzle_input)
    assert subject.part1(data) == 2
    data = subject.parse_lines(puzzle_input2)
    assert subject.part1(data) == 6

def test_part2_example1(puzzle_input3):
    data = subject.parse_lines(puzzle_input3)
    assert subject.part2(data) == 6

