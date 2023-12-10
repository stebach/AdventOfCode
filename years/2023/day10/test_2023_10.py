import solve_2023_10 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        ".....",
        ".S-7.",
        ".|.|.",
        ".L-J.",
        "....."
    ]

@pytest.fixture
def puzzle_input2():
    return [
        "..F7.",
        ".FJ|.",
        "SJ.L7",
        "|F--J",
        "LJ..."
    ]

@pytest.fixture
def puzzle_input3():
    return [
        "...........",
        ".S-------7.",
        ".|F-----7|.",
        ".||.....||.",
        ".||.....||.",
        ".|L-7.F-J|.",
        ".|..|.|..|.",
        ".L--J.L--J.",
        "..........."
    ]

@pytest.fixture
def puzzle_input4():
    return [
        ".F----7F7F7F7F-7....",
        ".|F--7||||||||FJ....",
        ".||.FJ||||||||L7....",
        "FJL7L7LJLJ||LJ.L-7..",
        "L--J.L7...LJS7F-7L7.",
        "....F-J..F7FJ|L7L7L7",
        "....L7.F7||L7|.L7L7|",
        ".....|FJLJ|FJ|F7|.LJ",
        "....FJL-7.||.||||...",
        "....L---J.LJ.LJLJ..."
    ]

@pytest.fixture
def puzzle_input5():
    return [
        "FF7FSF7F7F7F7F7F---7",
        "L|LJ||||||||||||F--J",
        "FL-7LJLJ||||||LJL-77",
        "F--JF--7||LJLJ7F7FJ-",
        "L---JF-JLJ.||-FJLJJ7",
        "|F|F-JF---7F7-L7L|7|",
        "|FFJF7L7F-JF7|JL---7",
        "7-L-JL7||F7|L7F-7F7|",
        "L.L7LFJ|||||FJL7||LJ",
        "L7JLJL-JLJLJL--JLJ.L"
    ]

def test_part1_example1(puzzle_input, puzzle_input2):
    assert subject.part1(puzzle_input) == 4
    assert subject.part1(puzzle_input2) == 8


def test_part2_example1(puzzle_input3, puzzle_input4, puzzle_input5):
    assert subject.part2(puzzle_input3) == 4
    assert subject.part2(puzzle_input4) == 8
    assert subject.part2(puzzle_input5) == 10
