import solve_2023_05 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'seeds': [79, 14, 55, 13],
        'seed-to-soil': [
            [[98,100], -48],
            [[50, 98], 2],
        ],
        'soil-to-fertilizer': [
            [[15, 52], -15],
            [[52, 54], -15],
            [[0, 15], 39]
        ],
        'fertilizer-to-water': [
            [[53, 61], -4],
            [[11, 53], -11],
            [[0, 7], 42],
            [[7, 11], 50],
        ],
        'water-to-light': [
            [[18, 25], 70],
            [[25, 95], -7]
        ],
        'light-to-temperature': [
            [[77, 100], -32],
            [[45, 64], 36],
            [[64, 77], 4]
        ],
        'temperature-to-humidity': [
            [[69, 70], -69],
            [[0, 69], 1]
        ],
        'humidity-to-location': [
            [[56, 56+37], 4],
            [[93, 93+4], -37],
        ]
    };

def test_seed_to_location(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.seed_to_location(79, data) == 82
    assert subject.seed_to_location(14, data) == 43
    assert subject.seed_to_location(55, data) == 86
    assert subject.seed_to_location(13, data) == 35

def test_part1_example1(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.part1(data) == 35

def test_part2_example1(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.part2(data, 10) == 46

