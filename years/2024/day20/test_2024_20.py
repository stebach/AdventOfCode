import solve_2024_20 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '###############',
        '#...#...#.....#',
        '#.#.#.#.#.###.#',
        '#S#...#.#.#...#',
        '#######.#.#.###',
        '#######.#.#...#',
        '#######.#.###.#',
        '###..E#...#...#',
        '###.#######.###',
        '#...###...#...#',
        '#.#####.#.###.#',
        '#.#...#.#.#...#',
        '#.#.#.#.#.#.###',
        '#...#...#...###',
        '###############'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'),
        ('#','.','.','.','#','.','.','.','#','.','.','.','.','.','#'),
        ('#','.','#','.','#','.','#','.','#','.','#','#','#','.','#'),
        ('#','S','#','.','.','.','#','.','#','.','#','.','.','.','#'),
        ('#','#','#','#','#','#','#','.','#','.','#','.','#','#','#'),
        ('#','#','#','#','#','#','#','.','#','.','#','.','.','.','#'),
        ('#','#','#','#','#','#','#','.','#','.','#','#','#','.','#'),
        ('#','#','#','.','.','E','#','.','.','.','#','.','.','.','#'),
        ('#','#','#','.','#','#','#','#','#','#','#','.','#','#','#'),
        ('#','.','.','.','#','#','#','.','.','.','#','.','.','.','#'),
        ('#','.','#','#','#','#','#','.','#','.','#','#','#','.','#'),
        ('#','.','#','.','.','.','#','.','#','.','#','.','.','.','#'),
        ('#','.','#','.','#','.','#','.','#','.','#','.','#','#','#'),
        ('#','.','.','.','#','.','.','.','#','.','.','.','#','#','#'),
        ('#','#','#','#','#','#','#','#','#','#','#','#','#','#','#')
    )

def test_find_cheats(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.find_cheats(data, 20) == 5
    assert subject.find_cheats(data, 10) == 10
    assert subject.find_cheats(data, 4) == 30

    assert subject.find_cheats(data, 76, 20) == 3
    assert subject.find_cheats(data, 74, 20) == 7
    assert subject.find_cheats(data, 72, 20) == 29
    assert subject.find_cheats(data, 60, 20) == 129

