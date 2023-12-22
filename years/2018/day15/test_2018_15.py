import solve_2018_15 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '#######',
        '#.G...#',
        '#...EG#',
        '#.#.#G#',
        '#..G#E#',
        '#.....#',
        '#######'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        '#######',
        '#G..#E#',
        '#E#E.E#',
        '#G.##.#',
        '#...#E#',
        '#...E.#',
        '#######'
    ]

@pytest.fixture
def puzzle_input3():
    return [
        '#######',
        '#E..EG#',
        '#.#G.E#',
        '#E.##E#',
        '#G..#.#',
        '#..E#.#',
        '#######'
    ]

@pytest.fixture
def puzzle_input4():
    return [
        '#######',
        '#E.G#.#',
        '#.#G..#',
        '#G.#.G#',
        '#G..#.#',
        '#...E.#',
        '#######'
    ]

@pytest.fixture
def puzzle_input5():
    return [
        '#######',
        '#.E...#',
        '#.#..G#',
        '#.###.#',
        '#E#G#G#',
        '#...#G#',
        '#######'
    ]

@pytest.fixture
def puzzle_input6():
    return [
        '#########',
        '#G......#',
        '#.E.#...#',
        '#..##..G#',
        '#...##..#',
        '#...#...#',
        '#.G...G.#',
        '#.....G.#',
        '#########'
    ]


def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'walls': ((0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,0),(1,6),(2,0),(2,6),(3,0),(3,2),(3,4),(3,6),(4,0),(4,4),(4,6),(5,0),(5,6),(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6)),
        'units': [
            [(1,2),'G',3,200],
            [(2,4),'E',3,200],
            [(2,5),'G',3,200],
            [(3,5),'G',3,200],
            [(4,3),'G',3,200],
            [(4,5),'E',3,200],
        ]
    }

def test_part1_example1(puzzle_input):
    assert subject.part1(subject.parse_lines(puzzle_input)) == 27730

def test_part1_example2(puzzle_input2):
    assert subject.part1(subject.parse_lines(puzzle_input2)) == 36334

def test_part1_example3(puzzle_input3):
    assert subject.part1(subject.parse_lines(puzzle_input3)) == 39514

def test_part1_example4(puzzle_input4):
    assert subject.part1(subject.parse_lines(puzzle_input4)) == 27755

def test_part1_example5(puzzle_input5):
    assert subject.part1(subject.parse_lines(puzzle_input5)) == 28944

def test_part1_example6(puzzle_input6):
    assert subject.part1(subject.parse_lines(puzzle_input6)) == 18740

def test_part2_example1(puzzle_input):
    assert subject.part2(subject.parse_lines(puzzle_input)) == 4988

def test_part2_example2(puzzle_input3):
    assert subject.part2(subject.parse_lines(puzzle_input3)) == 31284

def test_part2_example3(puzzle_input4):
    assert subject.part2(subject.parse_lines(puzzle_input4)) == 3478

def test_part2_example4(puzzle_input5):
    assert subject.part2(subject.parse_lines(puzzle_input5)) == 6474

def test_part2_example5(puzzle_input6):
    assert subject.part2(subject.parse_lines(puzzle_input6)) == 1140


