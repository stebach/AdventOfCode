import solve_2018_12 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'initial state: #..#.#..##......###...###',
        '',
        '...## => #',
        '..#.. => #',
        '.#... => #',
        '.#.#. => #',
        '.#.## => #',
        '.##.. => #',
        '.#### => #',
        '#.#.# => #',
        '#.### => #',
        '##.#. => #',
        '##.## => #',
        '###.. => #',
        '###.# => #',
        '####. => #'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        '#..#.#..##......###...###',
        {
            '...##':'#',
            '..#..':'#',
            '.#...':'#',
            '.#.#.':'#',
            '.#.##':'#',
            '.##..':'#',
            '.####':'#',
            '#.#.#':'#',
            '#.###':'#',
            '##.#.':'#',
            '##.##':'#',
            '###..':'#',
            '###.#':'#',
            '####.':'#'
        }
    )

def test_part1_example1(puzzle_input):
    assert subject.part1(subject.parse_lines(puzzle_input)) == 325

