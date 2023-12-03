import solve_2023_03 as subject
import pytest

def test_part1_example1():
    puzzle_input = tuple([
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ]);
    numbers = subject.find_numbers(puzzle_input)
    assert numbers == [
        [467, [['*', 3, 1]]],
        [114, []],
        [35, [['*', 3, 1]]],
        [633, [['#', 6, 3]]],
        [617, [['*', 3, 4]]],
        [58, []],
        [592, [['+', 5, 5]]],
        [755, [['*', 5, 8]]],
        [664, [['$', 3, 8]]],
        [598, [['*', 5, 8]]],
    ]
    assert subject.part1(numbers) == 4361

def test_part2_example1():
    puzzle_input = tuple([
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ]);
    numbers = subject.find_numbers(puzzle_input)
    assert subject.part2(numbers) == 467835

