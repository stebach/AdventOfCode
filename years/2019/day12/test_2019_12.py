import solve_2019_12 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '<x=-1, y=0, z=2>',
        '<x=2, y=-10, z=-7>',
        '<x=4, y=-8, z=8>',
        '<x=3, y=5, z=-1>'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        '<x=-8, y=-10, z=0>',
        '<x=5, y=5, z=10>',
        '<x=2, y=-7, z=3>',
        '<x=9, y=-8, z=-3>'
    ]


def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        [-1,0,2,0,0,0],
        [2,-10,-7,0,0,0],
        [4,-8,8,0,0,0],
        [3,5,-1,0,0,0],
    )

def test_move(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    subject.move(data)
    assert data == (
        [ 2, -1,  1,  3, -1, -1],
        [ 3, -7, -4,  1,  3,  3],
        [ 1, -7,  5, -3,  1, -3],
        [ 2,  2,  0, -1, -3,  1],
    )

    subject.move(data)
    assert data == (
        [ 5, -3, -1,  3, -2, -2],
        [ 1, -2,  2, -2,  5,  6],
        [ 1, -4, -1,  0,  3, -6],
        [ 1, -4,  2, -1, -6,  2],
    )
    subject.move(data)
    assert data == (
        [ 5, -6, -1,  0, -3,  0],
        [ 0,  0,  6, -1,  2,  4],
        [ 2,  1, -5,  1,  5, -4],
        [ 1, -8,  2,  0, -4,  0],
    )
    subject.move(data)
    assert data == (
        [ 2, -8,  0, -3, -2,  1],
        [ 2,  1,  7,  2,  1,  1],
        [ 2,  3, -6,  0,  2, -1],
        [ 2, -9,  1,  1, -1, -1],
    )
    subject.move(data)
    assert data == (
        [-1, -9,  2, -3, -1,  2],
        [ 4,  1,  5,  2,  0, -2],
        [ 2,  2, -4,  0, -1,  2],
        [ 3, -7, -1,  1,  2, -2],
    )
    subject.move(data)
    assert data == (
        [-1, -7,  3,  0,  2,  1],
        [ 3,  0,  0, -1, -1, -5],
        [ 3, -2,  1,  1, -4,  5],
        [ 3, -4, -2,  0,  3, -1],
    )
    subject.move(data)
    assert data == (
        [ 2, -2,  1,  3,  5, -2],
        [ 1, -4, -4, -2, -4, -4],
        [ 3, -7,  5,  0, -5,  4],
        [ 2,  0,  0, -1,  4,  2],
    )
    subject.move(data)
    assert data == (
        [ 5,  2, -2,  3,  4, -3],
        [ 2, -7, -5,  1, -3, -1],
        [ 0, -9,  6, -3, -2,  1],
        [ 1,  1,  3, -1,  1,  3],
    )
    subject.move(data)
    assert data == (
        [ 5,  3, -4,  0,  1, -2],
        [ 2, -9, -3,  0, -2,  2],
        [ 0, -8,  4,  0,  1, -2],
        [ 1,  1,  5,  0,  0,  2],
    )
    subject.move(data)
    assert data == (
        [ 2,  1, -3, -3, -2,  1],
        [ 1, -8,  0, -1,  1,  3],
        [ 3, -6,  1,  3,  2, -3],
        [ 2,  0,  4,  1, -1, -1],
    )

def test_calc_energy(puzzle_input, puzzle_input2):
    data = tuple(map(subject.parse_line, puzzle_input))
    for x in range(10):
        subject.move(data)
    assert subject.calc_energy(data) == 179

    data = tuple(map(subject.parse_line, puzzle_input2))
    for x in range(100):
        subject.move(data)
    assert subject.calc_energy(data) == 1940

def test_find_repetition(puzzle_input, puzzle_input2):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.find_repetition(data) == 2772
    data = tuple(map(subject.parse_line, puzzle_input2))
    assert subject.find_repetition(data) == 4686774924
