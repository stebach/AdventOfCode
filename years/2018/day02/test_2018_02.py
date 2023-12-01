import solve_2018_02 as subject
import pytest

def test_part1_example1():
    puzzle_input = ["abcdef","bababc","abbcde","abcccd","aabcdd","abcdee","ababab"]
    assert subject.part1(puzzle_input) == 12

def test_part2_example1():
    puzzle_input = ["abcde","fghij","klmno","pqrst","fguij","axcye","wvxyz"]
    assert subject.part2(puzzle_input) == "fgij"

