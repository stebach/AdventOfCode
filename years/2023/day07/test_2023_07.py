import solve_2023_07 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483"
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == tuple([
        ["32T3K", 765, [3,2,10,3,13], 20302100313, [3,2,10,3,13], 20302100313],
        ["T55J5", 684, [10,5,5,11,5], 41005051105, [10,5,5,0,5], 61005050005],
        ["KK677", 28, [13,13,6,7,7], 31313060707, [13,13,6,7,7], 31313060707],
        ["KTJJT", 220, [13,10,11,11,10], 31310111110, [13,10,0,0,10], 61310000010],
        ["QQQJA", 483, [12,12,12,11,14], 41212121114, [12,12,12,0,14], 61212120014]
    ])

def test_part1_example1(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.part1(data) == 6440

def test_part2_example1(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.part2(data) == 5905

