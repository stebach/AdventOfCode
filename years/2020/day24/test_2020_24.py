import solve_2020_24 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "sesenwnenenewseeswwswswwnenewsewsw",
        "neeenesenwnwwswnenewnwwsewnenwseswesw",
        "seswneswswsenwwnwse",
        "nwnwneseeswswnenewneswwnewseswneseene",
        "swweswneswnenwsewnwneneseenw",
        "eesenwseswswnenwswnwnwsewwnwsene",
        "sewnenenenesenwsewnenwwwse",
        "wenwwweseeeweswwwnwwe",
        "wsweesenenewnwwnwsenewsenwwsesesenwne",
        "neeswseenwwswnwswswnw",
        "nenwswwsewswnenenewsenwsenwnesesenew",
        "enewnwewneswsewnwswenweswnenwsenwsw",
        "sweneswneswneneenwnewenewwneswswnese",
        "swwesenesewenwneswnwwneseswwne",
        "enesenwswwswneneswsenwnewswseenwsese",
        "wnwnesenesenenwwnenwsewesewsesesew",
        "nenewswnwewswnenesenwnesewesw",
        "eneswnwswnwsenenwnwnwwseeswneewsenese",
        "neswnwewnwnwseenwseesewsenwsweewe",
        "wseweeenwnesenwwwswnew"
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (-1, 2),
        (-2, -3),
        (0,3),
        (0,-2),
        (-1,-2),
        (-1,0),
        (-2,-3),
        (-2,0),
        (-1,-1),
        (-1,1),
        (-2,-2),
        (-2,-2),
        (0,-3),
        (-1,0),
        (2,2),
        (0,0),
        (-1,-2),
        (0,-2),
        (2,0),
        (-2,-1)
    )

def test_toggle(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    black = []
    for entry in data:
        subject.toggle(black, entry)
    assert len(black) == 10

def test_flip(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    black = []
    for entry in data:
        subject.toggle(black, entry)

    checks = {
        1: 15,
        2: 12,
        3: 25,
        4: 14,
        5: 23,
        6: 28,
        7: 41,
        8: 37,
        9: 49,
        10: 37,
        20: 132,
        30: 259,
        40: 406,
        50: 566,
        60: 788,
        70: 1106,
        80: 1373,
        90: 1844,
        100: 2208
    } 
    for flipcount in range(100):
        black = subject.flip(black)
        if flipcount + 1 in checks:
            assert len(black) == checks[flipcount + 1]


