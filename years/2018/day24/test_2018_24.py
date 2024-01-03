import solve_2018_24 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'Immune System:',
        '17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2',
        '989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3',
        '',
        'Infection:',
        '801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1',
        '4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4',
        ]

def test_parse_lines(puzzle_input):
    #power  / initiative 
    assert subject.parse_lines(puzzle_input) == [
        [
            [76619, 2, 'fire', 17, 4507, 5390, ('radiation','bludgeoning'), None ],
            [24725, 3, 'slashing', 989, 25, 1274, ('bludgeoning', 'slashing'), ('fire',)]
        ],
        [
            [92916, 1, 'bludgeoning', 801, 116, 4706, ('radiation',), None ],
            [53820, 4, 'slashing', 4485, 12, 2961, ('fire', 'cold'), ('radiation',)]
        ]
    ]

def test_part1_example1(puzzle_input):
    assert subject.part1(subject.parse_lines(puzzle_input)) == 5216

def test_part2_example1(puzzle_input):
    assert subject.part2(subject.parse_lines(puzzle_input)) == 51
1