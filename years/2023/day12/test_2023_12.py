import solve_2023_12 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "???.### 1,1,3",
        ".??..??...?##. 1,1,3",
        "?#?#?#?#?#?#?#? 1,3,1,6",
        "????.#...#... 4,1,1",
        "????.######..#####. 1,6,5",
        "?###???????? 3,2,1"
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == tuple([
        ['???.###',(1,1,3)],
        ['.??..??...?##.',(1,1,3)],
        ['?#?#?#?#?#?#?#?',(1,3,1,6)],
        ['????.#...#...',(4,1,1)],
        ['????.######..#####.',(1,6,5)],
        ['?###????????',(3,2,1)],
    ])

def test_count_arrangements():
    assert subject.count_arrangements('.' + '???.###' + '.',(1,1,3)) == 1
    assert subject.count_arrangements('.' + '.??..??...?##.' + '.',(1,1,3)) == 4
    assert subject.count_arrangements('.' + '?#?#?#?#?#?#?#?' + '.',(1,3,1,6)) == 1
    assert subject.count_arrangements('.' + '????.#...#...' + '.',(4,1,1)) == 1
    assert subject.count_arrangements('.' + '????.######..#####.' + '.',(1,6,5)) == 4
    assert subject.count_arrangements('.' + '?###????????' + '.',(3,2,1)) == 10

def test_part1_example1(puzzle_input):
    assert subject.part1(tuple(map(subject.parse_line, puzzle_input))) == 21

def test_unfold():
    assert subject.unfold(['.#',[1]]) == ['.#?.#?.#?.#?.#',[1,1,1,1,1]]
    assert subject.unfold(['???.###',[1,1,3]]) == ['???.###????.###????.###????.###????.###',[1,1,3,1,1,3,1,1,3,1,1,3,1,1,3]]

def test_part2_example1(puzzle_input):
    assert subject.part2(tuple(map(subject.parse_line, puzzle_input))) == 525152
