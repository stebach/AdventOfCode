import solve_2018_03 as subject
import pytest

def test_part1_example1():
    puzzle_input = ["#1 @ 1,3: 4x4","#2 @ 3,1: 4x4","#3 @ 5,5: 2x2"]
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.part1(data) == 4

def test_part2_example1():
    puzzle_input = ["#1 @ 1,3: 4x4","#2 @ 3,1: 4x4","#3 @ 5,5: 2x2"]
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.part2(data) == 3

