import solve_2021_12 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end"
    ]

@pytest.fixture
def puzzle_input2():
    return [
        "dc-end",
        "HN-start",
        "start-kj",
        "dc-start",
        "dc-HN",
        "LN-dc",
        "HN-end",
        "kj-sa",
        "kj-HN",
        "kj-dc"
    ]

@pytest.fixture
def puzzle_input3():
    return [
        "fs-end",
        "he-DX",
        "fs-he",
        "start-DX",
        "pj-DX",
        "end-zg",
        "zg-sl",
        "zg-pj",
        "pj-he",
        "RW-he",
        "fs-DX",
        "pj-RW",
        "zg-RW",
        "start-pj",
        "he-WI",
        "zg-he",
        "pj-fs",
        "start-RW"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        {
            'start':['A','b'],
            'A':['start','c','b','end'],
            'end':['A','b'],
            'c':['A'],
            'b':['start','A','d','end'],
            'd':['b']
        },
        ['b','c','d']
    )

def test_count_paths(puzzle_input, puzzle_input2, puzzle_input3):
    data = subject.parse_lines(puzzle_input)
    assert subject.count_paths(data) == 10
    assert subject.count_paths(data, True) == 36

    data = subject.parse_lines(puzzle_input2)
    assert subject.count_paths(data) == 19
    assert subject.count_paths(data, True) == 103

    data = subject.parse_lines(puzzle_input3)
    assert subject.count_paths(data) == 226
    assert subject.count_paths(data, True) == 3509


