import solve_2019_03 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "R8,U5,L5,D3",
        "U7,R6,D4,L4"
    ]

@pytest.fixture
def puzzle_input2():
    return [
        "R75,D30,R83,U83,L12,D49,R71,U7,L72",
        "U62,R66,U55,R34,D71,R55,D58,R83"
    ]

@pytest.fixture
def puzzle_input3():
    return [
        "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
        "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    ]

def test_parse_line(puzzle_input, puzzle_input3):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (('R',8),('U',5),('L',5),('D',3)),
        (('U',7),('R',6),('D',4),('L',4))
    )
    assert tuple(map(subject.parse_line, puzzle_input3)) == (
        (('R',98),('U',47),('R',26),('D',63),('R',33),('U',87),('L',62),('D',20),('R',33),('U',53),('R',51)),
        (('U',98),('R',91),('D',20),('R',16),('D',67),('R',40),('U',7),('R',15),('U',6),('R',7))
    )

def test_part1(puzzle_input, puzzle_input2, puzzle_input3):
    assert subject.part1(tuple(map(subject.parse_line, puzzle_input))) == 6
    assert subject.part1(tuple(map(subject.parse_line, puzzle_input2))) ==159
    assert subject.part1(tuple(map(subject.parse_line, puzzle_input3))) == 135

def test_part2(puzzle_input, puzzle_input2, puzzle_input3):
    assert subject.part2(tuple(map(subject.parse_line, puzzle_input))) == 30
    assert subject.part2(tuple(map(subject.parse_line, puzzle_input2))) == 610
    assert subject.part2(tuple(map(subject.parse_line, puzzle_input3))) == 410
