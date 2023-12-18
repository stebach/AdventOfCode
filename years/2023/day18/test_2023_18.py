import solve_2023_18 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'R 6 (#70c710)',
        'D 5 (#0dc571)',
        'L 2 (#5713f0)',
        'D 2 (#d2c081)',
        'R 2 (#59c680)',
        'D 2 (#411b91)',
        'L 5 (#8ceee2)',
        'U 2 (#caa173)',
        'L 1 (#1b58a2)',
        'U 2 (#caa171)',
        'R 2 (#7807d2)',
        'U 3 (#a77fa3)',
        'L 2 (#015232)',
        'U 2 (#7a21e3)'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ((1,0),6,'#70c710'),
        ((0,1),5,'#0dc571'),
        ((-1,0),2,'#5713f0'),
        ((0,1),2,'#d2c081'),
        ((1,0),2,'#59c680'),
        ((0,1),2,'#411b91'),
        ((-1,0),5,'#8ceee2'),
        ((0,-1),2,'#caa173'),
        ((-1,0),1,'#1b58a2'),
        ((0,-1),2,'#caa171'),
        ((1,0),2,'#7807d2'),
        ((0,-1),3,'#a77fa3'),
        ((-1,0),2,'#015232'),
        ((0,-1),2,'#7a21e3')
    )

def test_part2_translate():
    assert subject.translate(((1,0),6,'#70c710')) == ((1,0),461937)
    assert subject.translate(((0,1),5,'#0dc571')) == ((0,1), 56407)
    assert subject.translate(((-1,0),2,'#5713f0')) == ((1,0), 356671)
    assert subject.translate(((0,1),2,'#d2c081')) == ((0,1), 863240)
    assert subject.translate(((-1,0),5,'#8ceee2')) == ((-1,0), 577262)
    assert subject.translate(((0,-1),2,'#caa173')) == ((0,-1), 829975)


def test_part1_example1(puzzle_input):
    assert subject.part1(tuple(map(subject.parse_line,puzzle_input))) == 62

def test_part2_example1(puzzle_input):
    assert subject.part2(tuple(map(subject.parse_line,puzzle_input))) == 952408144115

