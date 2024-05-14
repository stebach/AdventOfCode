import solve_2015_19 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'H => HO',
        'H => OH',
        'O => HH',
        '',
        'HOH'
]

@pytest.fixture
def puzzle_input2():
    return [
        'H => HO',
        'H => OH',
        'O => HH',
        '',
        'HOHOHO'
]

@pytest.fixture
def puzzle_input3():
    return [
        'e => H',
        'e => O',
        'H => HO',
        'H => OH',
        'O => HH',
        '',
        'HOH'
]

@pytest.fixture
def puzzle_input4():
    return [
        'e => H',
        'e => O',
        'H => HO',
        'H => OH',
        'O => HH',
        '',
        'HOHOHO'
]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        {
            'H': ('HO','OH'),
            'O': ('HH',),
        },
        'HOH'
    )

def test_count_distinct_molecules(puzzle_input, puzzle_input2):
    data = subject.parse_lines(puzzle_input)
    data2 = subject.parse_lines(puzzle_input2)
    assert subject.count_distinct_molecules(data) == 4
    assert subject.count_distinct_molecules(data2) == 7

def test_count_steps_ot_create(puzzle_input3, puzzle_input4):
    data = subject.parse_lines(puzzle_input3)
    data2 = subject.parse_lines(puzzle_input4)
    assert subject.count_steps_to_create(data) == 3
    assert subject.count_steps_to_create(data2) == 6
