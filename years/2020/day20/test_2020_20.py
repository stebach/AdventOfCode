import solve_2020_20 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "Tile 2311:",
        "..##.#..#.",
        "##..#.....",
        "#...##..#.",
        "####.#...#",
        "##.##.###.",
        "##...#.###",
        ".#.#.#..##",
        "..#....#..",
        "###...#.#.",
        "..###..###",
        "",
        "Tile 1951:",
        "#.##...##.",
        "#.####...#",
        ".....#..##",
        "#...######",
        ".##.#....#",
        ".###.#####",
        "###.##.##.",
        ".###....#.",
        "..#.#..#.#",
        "#...##.#..",
        "",
        "Tile 1171:",
        "####...##.",
        "#..##.#..#",
        "##.#..#.#.",
        ".###.####.",
        "..###.####",
        ".##....##.",
        ".#...####.",
        "#.##.####.",
        "####..#...",
        ".....##...",
        "",
        "Tile 1427:",
        "###.##.#..",
        ".#..#.##..",
        ".#.##.#..#",
        "#.#.#.##.#",
        "....#...##",
        "...##..##.",
        "...#.#####",
        ".#.####.#.",
        "..#..###.#",
        "..##.#..#.",
        "",
        "Tile 1489:",
        "##.#.#....",
        "..##...#..",
        ".##..##...",
        "..#...#...",
        "#####...#.",
        "#..#.#.#.#",
        "...#.#.#..",
        "##.#...##.",
        "..##.##.##",
        "###.##.#..",
        "",
        "Tile 2473:",
        "#....####.",
        "#..#.##...",
        "#.##..#...",
        "######.#.#",
        ".#...#.#.#",
        ".#########",
        ".###.#..#.",
        "########.#",
        "##...##.#.",
        "..###.#.#.",
        "",
        "Tile 2971:",
        "..#.#....#",
        "#...###...",
        "#.#.###...",
        "##.##..#..",
        ".#####..##",
        ".#..####.#",
        "#..#.#..#.",
        "..####.###",
        "..#.#.###.",
        "...#.#.#.#",
        "",
        "Tile 2729:",
        "...#.#.#.#",
        "####.#....",
        "..#.#.....",
        "....#..#.#",
        ".##..##.#.",
        ".#.####...",
        "####.#.#..",
        "##.####...",
        "##..#.##..",
        "#.##...##.",
        "",
        "Tile 3079:",
        "#.#.#####.",
        ".#..######",
        "..#.......",
        "######....",
        "####.#..#.",
        ".#...#.##.",
        "#.#####.##",
        "..#.###...",
        "..#.......",
        "..#.###..."
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == [
        {
            "id": 2311,
            "lines": [
                "..##.#..#.",
                "##..#.....",
                "#...##..#.",
                "####.#...#",
                "##.##.###.",
                "##...#.###",
                ".#.#.#..##",
                "..#....#..",
                "###...#.#.",
                "..###..###",
            ],
            "matches": [],
            "top":"..##.#..#.",
            "bottom":"###..###..",
            "left":".#..#####.",
            "right":"...#.##..#"
        },
        {
            "id": 1951,
            "lines": [
                "#.##...##.",
                "#.####...#",
                ".....#..##",
                "#...######",
                ".##.#....#",
                ".###.#####",
                "###.##.##.",
                ".###....#.",
                "..#.#..#.#",
                "#...##.#..",
            ],
            "matches": [],
            "top":"#.##...##.",
            "bottom":"..#.##...#",
            "left":"#..#..#.##",
            "right":".#####..#."
        },
        {
            "id": 1171,
            "lines": [
                "####...##.",
                "#..##.#..#",
                "##.#..#.#.",
                ".###.####.",
                "..###.####",
                ".##....##.",
                ".#...####.",
                "#.##.####.",
                "####..#...",
                ".....##...",
            ],
            "matches": [],
            "top":"####...##.",
            "bottom":"...##.....",
            "left":".##....###",
            "right":".#..#....."
        },
        {
            "id": 1427,
            "lines": [
                "###.##.#..",
                ".#..#.##..",
                ".#.##.#..#",
                "#.#.#.##.#",
                "....#...##",
                "...##..##.",
                "...#.#####",
                ".#.####.#.",
                "..#..###.#",
                "..##.#..#.",
            ],
            "matches": [],
            "top":"###.##.#..",
            "bottom":".#..#.##..",
            "left":"......#..#",
            "right":"..###.#.#."
        },
        {
            "id": 1489,
            "lines": [
                "##.#.#....",
                "..##...#..",
                ".##..##...",
                "..#...#...",
                "#####...#.",
                "#..#.#.#.#",
                "...#.#.#..",
                "##.#...##.",
                "..##.##.##",
                "###.##.#..",
            ],
            "matches": [],
            "top":"##.#.#....",
            "bottom":"..#.##.###",
            "left":"#.#.##...#",
            "right":".....#..#."
        },
        {
            "id": 2473,
            "lines": [
                "#....####.",
                "#..#.##...",
                "#.##..#...",
                "######.#.#",
                ".#...#.#.#",
                ".#########",
                ".###.#..#.",
                "########.#",
                "##...##.#.",
                "..###.#.#.",
            ],
            "matches": [],
            "top":"#....####.",
            "bottom":".#.#.###..",
            "left":".##...####",
            "right":"...###.#.."
        },
        {
            "id": 2971,
            "lines": [
                "..#.#....#",
                "#...###...",
                "#.#.###...",
                "##.##..#..",
                ".#####..##",
                ".#..####.#",
                "#..#.#..#.",
                "..####.###",
                "..#.#.###.",
                "...#.#.#.#",
            ],
            "matches": [],
            "top":"..#.#....#",
            "bottom":"#.#.#.#...",
            "left":"...#..###.",
            "right":"#...##.#.#"
        },
        {
            "id": 2729,
            "lines": [
                "...#.#.#.#",
                "####.#....",
                "..#.#.....",
                "....#..#.#",
                ".##..##.#.",
                ".#.####...",
                "####.#.#..",
                "##.####...",
                "##..#.##..",
                "#.##...##.",
            ],
            "matches": [],
            "top":"...#.#.#.#",
            "bottom":".##...##.#",
            "left":"####....#.",
            "right":"#..#......"
        },
        {
            "id": 3079,
            "lines": [
                "#.#.#####.",
                ".#..######",
                "..#.......",
                "######....",
                "####.#..#.",
                ".#...#.##.",
                "#.#####.##",
                "..#.###...",
                "..#.......",
                "..#.###..."
            ],
            "matches": [],
            "top":"#.#.#####.",
            "bottom":"...###.#..",
            "left":"...#.##..#",
            "right":".#....#..."
        }
    ]

def test_arrange(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    subject.arrange(data)
    assert subject.get_corner_product(data) == 20899048083289

def test_draw_map(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.draw_map(data) == [
    ".####...#####..#...###..",
    "#####..#..#.#.####..#.#.",
    ".#.#...#.###...#.##.##..",
    "#.#.##.###.#.##.##.#####",
    "..##.###.####..#.####.##",
    "...#.#..##.##...#..#..##",
    "#.##.#..#.#..#..##.#.#..",
    ".###.##.....#...###.#...",
    "#.####.#.#....##.#..#.#.",
    "##...#..#....#..#...####",
    "..#.##...###..#.#####..#",
    "....#.##.#.#####....#...",
    "..##.##.###.....#.##..#.",
    "#...#...###..####....##.",
    ".#.##...#.##.#.#.###...#",
    "#.###.#..####...##..#...",
    "#.###...#.##...#.######.",
    ".###.###.#######..#####.",
    "..##.#..#..#.#######.###",
    "#.#..##.########..#..##.",
    "#.#####..#.#...##..#....",
    "#....##..#.#########..##",
    "#...#.....#..##...###.##",
    "#..###....##.#...##.##.#"
]

def test_get_roughness(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.get_roughness(data) == 273

