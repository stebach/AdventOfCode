import solve_2021_24 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "inp w",
        "add z w",
        "mod z 2",
        "div w 2",
        "add y w",
        "mod y 2",
        "div w 2",
        "add x w",
        "mod x 2",
        "div w 2",
        "mod w 2",
    ]

@pytest.fixture
def puzzle_input2():
    return [
        "inp z",
        "inp x",
        "mul z 3",
        "eql z x",
    ]


def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('inp','w'),
        ('add', 'z', 'w'),
        ('mod', 'z', 2),
        ('div', 'w', 2),
        ('add', 'y', 'w'),
        ('mod', 'y', 2),
        ('div', 'w', 2),
        ('add', 'x', 'w'),
        ('mod', 'x', 2),
        ('div', 'w', 2),
        ('mod', 'w', 2),
    )

def test_run(puzzle_input, puzzle_input2):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.run(data, [10]) == [1,0,1,0]

    data = tuple(map(subject.parse_line, puzzle_input2))
    assert subject.run(data, [1,3])[3] == 1
    assert subject.run(data, [1,6])[3] == 0
    assert subject.run(data, [2,6])[3] == 1

