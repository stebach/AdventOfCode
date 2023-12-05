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
            [range(98,100), -48],
            [range(50, 98), 2],
        ],
        'soil-to-fertilizer': [
            [range(15, 52), -15],
            [range(52, 54), -15],
            [range(0, 15), 39]
        ],
        'fertilizer-to-water': [
            [range(53, 61), -4],
            [range(11, 53), -11],
            [range(0, 7), 42],
            [range(7, 11), 50],
        ],
        'water-to-light': [
            [range(18, 25), 70],
            [range(25, 95), -7]
        ],
        'light-to-temperature': [
            [range(77, 100), -32],
            [range(45, 64), 36],
            [range(64, 77), 4]
        ],
        'temperature-to-humidity': [
            [range(69, 70), -69],
            [range(0, 69), 1]
        ],
        'humidity-to-location': [
            [range(56, 56+37), 4],
            [range(93, 93+4), -37],
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

def test_location_to_seed(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.location_to_seed(82, data) == 79
    assert subject.location_to_seed(43, data) == 14
    assert subject.location_to_seed(86, data) == 55
    assert subject.location_to_seed(35, data) == 13

def test_part2_example1(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.part2(data, 10) == 46

@pytest.mark.skip(reason="not yet implemented")
def test_part2_example2(puzzle_input):
    assert subject.part2(puzzle_input) == 1

@pytest.mark.skip(reason="not yet implemented")
def test_part2_example3(puzzle_input):
    assert subject.part2(puzzle_input) == 1

@pytest.mark.skip(reason="not yet implemented")
def test_part2_example4(puzzle_input):
    assert subject.part2(puzzle_input) == 1

