import solve as subject
import pytest

def test_part1_example1():
    puzzle_input = [+1, +1, +1]
    assert subject.part1(puzzle_input) == 3

def test_part1_example2():
    puzzle_input = [+1, +1, -2]
    assert subject.part1(puzzle_input) == 0

def test_part1_example3():
    puzzle_input = [-1, -2, -3]
    assert subject.part1(puzzle_input) == -6


def test_part2_example1():
    puzzle_input = [+1, -1]
    assert subject.part2(puzzle_input) == 0

def test_part2_example2():
    puzzle_input = [+3, +3, +4, -2, -4]
    assert subject.part2(puzzle_input) == 10

def test_part2_example3():
    puzzle_input = [-6, +3, +8, +5, -6]
    assert subject.part2(puzzle_input) == 5

def test_part2_example4():
    puzzle_input = [+7, +7, -2, -7, -4]
    assert subject.part2(puzzle_input) == 14

