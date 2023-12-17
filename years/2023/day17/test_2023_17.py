import solve_2023_17 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '2413432311323',
        '3215453535623',
        '3255245654254',
        '3446585845452',
        '4546657867536',
        '1438598798454',
        '4457876987766',
        '3637877979653',
        '4654967986887',
        '4564679986453',
        '1224686865563',
        '2546548887735',
        '4322674655533'
    ]

def test_part1_example1(puzzle_input):
    assert subject.part1(puzzle_input) == 102

@pytest.mark.skip(reason="not yet implemented")
def test_part1_example2(puzzle_input):
    assert subject.part1(puzzle_input) == 1

@pytest.mark.skip(reason="not yet implemented")
def test_part1_example3(puzzle_input):
    assert subject.part1(puzzle_input) == 1

@pytest.mark.skip(reason="not yet implemented")
def test_part1_example4(puzzle_input):
    assert subject.part1(puzzle_input) == 1

def test_part2_example1(puzzle_input):
    assert subject.part2(puzzle_input) == 1

@pytest.mark.skip(reason="not yet implemented")
def test_part2_example2(puzzle_input):
    assert subject.part2(puzzle_input) == 1

@pytest.mark.skip(reason="not yet implemented")
def test_part2_example3(puzzle_input):
    assert subject.part2(puzzle_input) == 1

@pytest.mark.skip(reason="not yet implemented")
def test_part2_example4(puzzle_input):
    assert subject.part2(puzzle_input) == 1

