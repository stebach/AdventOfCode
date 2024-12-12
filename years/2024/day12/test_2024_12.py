import solve_2024_12 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'AAAA',
        'BBCD',
        'BBCC',
        'EEEC'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        'OOOOO',
        'OXOXO',
        'OOOOO',
        'OXOXO',
        'OOOOO'
    ]

@pytest.fixture
def puzzle_input3():
    return [
        'RRRRIICCFF',
        'RRRRIICCCF',
        'VVRRRCCFFF',
        'VVRCCCJFFF',
        'VVVVCJJCFE',
        'VVIVCCJJEE',
        'VVIIICJJEE',
        'MIIIIIJJEE',
        'MIIISIJEEE',
        'MMMISSJEEE'
    ]

@pytest.fixture
def puzzle_input4():
    return [
        'EEEEE',
        'EXXXX',
        'EEEEE',
        'EXXXX',
        'EEEEE'
    ]

@pytest.fixture
def puzzle_input5():
    return [
        'AAAAAA',
        'AAABBA',
        'AAABBA',
        'ABBAAA',
        'ABBAAA',
        'AAAAAA'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('A','A','A','A'),
        ('B','B','C','D'),
        ('B','B','C','C'),
        ('E','E','E','C')
    )

def test_calc_fencing_price(puzzle_input, puzzle_input2, puzzle_input3, puzzle_input4, puzzle_input5):
    data = tuple(map(subject.parse_line, puzzle_input))
    data2 = tuple(map(subject.parse_line, puzzle_input2))
    data3 = tuple(map(subject.parse_line, puzzle_input3))
    data4 = tuple(map(subject.parse_line, puzzle_input4))
    data5 = tuple(map(subject.parse_line, puzzle_input5))

    assert subject.calc_fencing_price(data) == 140
    assert subject.calc_fencing_price(data2) == 772
    assert subject.calc_fencing_price(data3) == 1930

    assert subject.calc_fencing_price(data, True) == 80
    assert subject.calc_fencing_price(data2, True) == 436
    assert subject.calc_fencing_price(data3, True) == 1206
    assert subject.calc_fencing_price(data4, True) == 236
    assert subject.calc_fencing_price(data5, True) == 368

def test_solve(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.solve(data) == (140, 80)

