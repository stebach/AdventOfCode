import solve_2019_10 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '.#..#',
        '.....',
        '#####',
        '....#',
        '...##'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        '......#.#.',
        '#..#.#....',
        '..#######.',
        '.#.#.###..',
        '.#..#.....',
        '..#....#.#',
        '#..#....#.',
        '.##.#..###',
        '##...#..#.',
        '.#....####'
    ]

@pytest.fixture
def puzzle_input3():
    return [
        '#.#...#.#.',
        '.###....#.',
        '.#....#...',
        '##.#.#.#.#',
        '....#.#.#.',
        '.##..###.#',
        '..#...##..',
        '..##....##',
        '......#...',
        '.####.###.'
    ]

@pytest.fixture
def puzzle_input4():
    return [
        '.#..#..###',
        '####.###.#',
        '....###.#.',
        '..###.##.#',
        '##.##.#.#.',
        '....###..#',
        '..#.#..#.#',
        '#..#.#.###',
        '.##...##.#',
        '.....#.#..'
    ]

@pytest.fixture
def puzzle_input5():
    return [
        '.#..##.###...#######',
        '##.############..##.',
        '.#.######.########.#',
        '.###.#######.####.#.',
        '#####.##.#.##.###.##',
        '..#####..#.#########',
        '####################',
        '#.####....###.#.#.##',
        '##.#################',
        '#####.##.###..####..',
        '..######..##.#######',
        '####.##.####...##..#',
        '.#####..#.######.###',
        '##...#.##########...',
        '#.##########.#######',
        '.####.#.###.###.#.##',
        '....##.##.###..#####',
        '.#.#.###########.###',
        '#.#.#.#####.####.###',
        '###.##.####.##.#..##'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        (1,0),(4,0),(0,2),(1,2),(2,2),(3,2),(4,2),(4,3),(3,4),(4,4)
    )

def test_part1(puzzle_input, puzzle_input2, puzzle_input3, puzzle_input4, puzzle_input5):
    assert subject.part1(subject.parse_lines(puzzle_input)) == 8
    assert subject.part1(subject.parse_lines(puzzle_input2)) == 33
    assert subject.part1(subject.parse_lines(puzzle_input3)) == 35
    assert subject.part1(subject.parse_lines(puzzle_input4)) == 41
    assert subject.part1(subject.parse_lines(puzzle_input5)) == 210

def test_part2(puzzle_input5):
    assert subject.part2(subject.parse_lines(puzzle_input5)) == 802

