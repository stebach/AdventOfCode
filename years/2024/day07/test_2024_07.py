import solve_2024_07 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '190: 10 19',
        '3267: 81 40 27',
        '83: 17 5',
        '156: 15 6',
        '7290: 6 8 6 15',
        '161011: 16 10 13',
        '192: 17 8 14',
        '21037: 9 7 18 13',
        '292: 11 6 16 20'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        {
            'test_value': 190,
            'numbers': (10, 19)
        },
        {
            'test_value': 3267,
            'numbers': (81, 40, 27)
        },
        {
            'test_value': 83,
            'numbers': (17, 5)
        },
        {
            'test_value': 156,
            'numbers': (15, 6)
        },
        {
            'test_value': 7290,
            'numbers': (6, 8, 6, 15)
        },
        {
            'test_value': 161011,
            'numbers': (16, 10, 13)
        },
        {
            'test_value': 192,
            'numbers': (17, 8, 14)
        },
        {
            'test_value': 21037,
            'numbers': (9, 7, 18, 13)
        },
        {
            'test_value': 292,
            'numbers': (11, 6, 16, 20)
        }
    )

def test_check_equation(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.check_equation(data[0]) == True
    assert subject.check_equation(data[1]) == True
    assert subject.check_equation(data[2]) == False
    assert subject.check_equation(data[3]) == False
    assert subject.check_equation(data[4]) == False
    assert subject.check_equation(data[5]) == False
    assert subject.check_equation(data[6]) == False
    assert subject.check_equation(data[7]) == False
    assert subject.check_equation(data[8]) == True

    assert subject.check_equation(data[0], True) == True
    assert subject.check_equation(data[1], True) == True
    assert subject.check_equation(data[2], True) == False
    assert subject.check_equation(data[3], True) == True
    assert subject.check_equation(data[4], True) == True
    assert subject.check_equation(data[5], True) == False
    assert subject.check_equation(data[6], True) == True
    assert subject.check_equation(data[7], True) == False
    assert subject.check_equation(data[8], True) == True

def test_solve(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.solve(data) == (3749, 11387)

