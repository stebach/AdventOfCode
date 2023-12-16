import solve_2023_16 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '.|...\\....',
        '|.-.\\.....',
        '.....|-...',
        '........|.',
        '..........',
        '.........\\',
        '..../.\\\\..',
        '.-.-/..|..',
        '.|....-|.\\',
        '..//.|....'
        ]


def test_part1_example1(puzzle_input):
    assert subject.part1(puzzle_input) == 46

def test_part2_example1(puzzle_input):
    assert subject.part2(puzzle_input) == 51
