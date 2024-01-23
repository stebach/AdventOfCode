import solve_2020_02 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '1-3 a: abcde',
        '1-3 b: cdefg',
        '2-9 c: ccccccccc'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (1,3,'a','abcde'),
        (1,3,'b','cdefg'),
        (2,9,'c','ccccccccc'),
    )

def test_check_password(puzzle_input):
    assert subject.check_password((1,3,'a','abcde')) == True
    assert subject.check_password((1,3,'b','cdefg')) == False
    assert subject.check_password((2,9,'c','ccccccccc')) == True

def test_check_password_part2(puzzle_input):
    assert subject.check_password_part2((1,3,'a','abcde')) == True
    assert subject.check_password_part2((1,3,'b','cdefg')) == False
    assert subject.check_password_part2((2,9,'c','ccccccccc')) == False

