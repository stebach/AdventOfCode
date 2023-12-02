import solve_2023_02 as subject
import pytest

def test_process_draw():
    assert subject.process_draw("3 blue, 4 red") == [4, 0, 3]
    assert subject.process_draw("1 red, 2 green, 6 blue") ==  [1, 2, 6]
    assert subject.process_draw("2 green") ==  [0, 2, 0]

def test_process_line():
    assert subject.process_line("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == tuple([1, [[4,0,3],[1,2,6],[0,2,0]]])
    assert subject.process_line("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue") == tuple([2, [[0, 2, 1], [1, 3, 4], [0, 1, 1]]])
    assert subject.process_line("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red") == tuple([3, [[20, 8, 6],[4, 13, 5],[1,5,0]]])

def test_part1_example1():
    puzzle_input = tuple(map(subject.process_line, [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    ]))
    assert subject.part1(puzzle_input) == 8

def test_part2_example1():
    puzzle_input = tuple(map(subject.process_line, [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    ]))
    assert subject.part2(puzzle_input) == 2286

@pytest.mark.skip(reason="not yet implemented")
def test_part2_example2():
    puzzle_input = [1,2,3]
    assert subject.part2(puzzle_input) == 1

@pytest.mark.skip(reason="not yet implemented")
def test_part2_example3():
    puzzle_input = [1,2,3]
    assert subject.part2(puzzle_input) == 1

@pytest.mark.skip(reason="not yet implemented")
def test_part2_example4():
    puzzle_input = [1,2,3]
    assert subject.part2(puzzle_input) == 1

