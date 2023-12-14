import solve_2023_14 as subject
import pytest
from functools import cmp_to_key


@pytest.fixture
def puzzle_input():
    return tuple([tuple([y for y in x]) for x in [
        'O....#....',
        'O.OO#....#',
        '.....##...',
        'OO.#O....O',
        '.O.....O#.',
        'O.#..O.#.#',
        '..O..#O..O',
        '.......O..',
        '#....###..',
        '#OO..#....'
    ]])

def test_sort():
    assert subject.move_rocks(('#','#','.','O','.','O')) == ('#','#','.','.','O','O')
    assert subject.move_rocks(('#','O','.','O','.','O')) == ('#','.','.','O','O','O')
    assert subject.move_rocks(('O','#','.','O','.','O')) == ('O','#','.','.','O','O')
    assert subject.move_rocks(('O','.','#','O','.','O')) == ('.','O','#','.','O','O')


def test_tilt(puzzle_input):
    assert subject.tilt(puzzle_input) == tuple([tuple([y for y in x]) for x in [
        'OOOO.#.O..',
        'OO..#....#',
        'OO..O##..O',
        'O..#.OO...',
        '........#.',
        '..#....#.#',
        '..O..#.O.O',
        '..O.......',
        '#....###..',
        '#....#....'
    ]])
    assert subject.tilt(puzzle_input, True) == tuple([tuple([y for y in x]) for x in [
        '.....#....',
        '....#...O#',
        '...OO##...',
        '.OO#......',
        '.....OOO#.',
        '.O#...O#.#',
        '....O#....',
        '......OOOO',
        '#...O###..',
        '#..OO#....'
    ]])

    assert subject.tilt(subject.tilt(puzzle_input, True), True) == tuple([tuple([y for y in x]) for x in [
        '.....#....',
        '....#...O#',
        '.....##...',
        '..O#......',
        '.....OOO#.',
        '.O#...O#.#',
        '....O#...O',
        '.......OOO',
        '#..OO###..',
        '#.OOO#...O'
    ]])

    assert subject.tilt(subject.tilt(subject.tilt(puzzle_input, True), True), True) == tuple([tuple([y for y in x]) for x in [
        '.....#....',
        '....#...O#',
        '.....##...',
        '..O#......',
        '.....OOO#.',
        '.O#...O#.#',
        '....O#...O',
        '.......OOO',
        '#...O###.O',
        '#.OOO#...O'
    ]])

def test_part1_example1(puzzle_input):
    assert subject.part1(puzzle_input) == 136

def test_part2_example1(puzzle_input):
    assert subject.part2(puzzle_input) == 64
