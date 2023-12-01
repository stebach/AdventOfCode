import solve_2022_01 as subject
import pytest

def test_part1_example1():
    puzzle_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    assert subject.part1(subject.parse_data(puzzle_input)) == 24000

def test_part2_example1():
    puzzle_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    assert subject.part2(subject.parse_data(puzzle_input)) == 45000

