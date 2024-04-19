import solve_2022_10 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "addx 15",
        "addx -11",
        "addx 6",
        "addx -3",
        "addx 5",
        "addx -1",
        "addx -8",
        "addx 13",
        "addx 4",
        "noop",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx -35",
        "addx 1",
        "addx 24",
        "addx -19",
        "addx 1",
        "addx 16",
        "addx -11",
        "noop",
        "noop",
        "addx 21",
        "addx -15",
        "noop",
        "noop",
        "addx -3",
        "addx 9",
        "addx 1",
        "addx -3",
        "addx 8",
        "addx 1",
        "addx 5",
        "noop",
        "noop",
        "noop",
        "noop",
        "noop",
        "addx -36",
        "noop",
        "addx 1",
        "addx 7",
        "noop",
        "noop",
        "noop",
        "addx 2",
        "addx 6",
        "noop",
        "noop",
        "noop",
        "noop",
        "noop",
        "addx 1",
        "noop",
        "noop",
        "addx 7",
        "addx 1",
        "noop",
        "addx -13",
        "addx 13",
        "addx 7",
        "noop",
        "addx 1",
        "addx -33",
        "noop",
        "noop",
        "noop",
        "addx 2",
        "noop",
        "noop",
        "noop",
        "addx 8",
        "noop",
        "addx -1",
        "addx 2",
        "addx 1",
        "noop",
        "addx 17",
        "addx -9",
        "addx 1",
        "addx 1",
        "addx -3",
        "addx 11",
        "noop",
        "noop",
        "addx 1",
        "noop",
        "addx 1",
        "noop",
        "noop",
        "addx -13",
        "addx -19",
        "addx 1",
        "addx 3",
        "addx 26",
        "addx -30",
        "addx 12",
        "addx -1",
        "addx 3",
        "addx 1",
        "noop",
        "noop",
        "noop",
        "addx -9",
        "addx 18",
        "addx 1",
        "addx 2",
        "noop",
        "noop",
        "addx 9",
        "noop",
        "noop",
        "noop",
        "addx -1",
        "addx 2",
        "addx -37",
        "addx 1",
        "addx 3",
        "noop",
        "addx 15",
        "addx -21",
        "addx 22",
        "addx -6",
        "addx 1",
        "noop",
        "addx 2",
        "addx 1",
        "noop",
        "addx -10",
        "noop",
        "noop",
        "addx 20",
        "addx 1",
        "addx 2",
        "addx 2",
        "addx -6",
        "addx -11",
        "noop",
        "noop",
        "noop",
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (2,15),
        (2,-11),
        (2,6),
        (2,-3),
        (2,5),
        (2,-1),
        (2,-8),
        (2,13),
        (2,4),
        (1,),
        (2,-1),
        (2,5),
        (2,-1),
        (2,5),
        (2,-1),
        (2,5),
        (2,-1),
        (2,5),
        (2,-1),
        (2,-35),
        (2,1),
        (2,24),
        (2,-19),
        (2,1),
        (2,16),
        (2,-11),
        (1,),
        (1,),
        (2,21),
        (2,-15),
        (1,),
        (1,),
        (2,-3),
        (2,9),
        (2,1),
        (2,-3),
        (2,8),
        (2,1),
        (2,5),
        (1,),
        (1,),
        (1,),
        (1,),
        (1,),
        (2,-36),
        (1,),
        (2,1),
        (2,7),
        (1,),
        (1,),
        (1,),
        (2,2),
        (2,6),
        (1,),
        (1,),
        (1,),
        (1,),
        (1,),
        (2,1),
        (1,),
        (1,),
        (2,7),
        (2,1),
        (1,),
        (2,-13),
        (2,13),
        (2,7),
        (1,),
        (2,1),
        (2,-33),
        (1,),
        (1,),
        (1,),
        (2,2),
        (1,),
        (1,),
        (1,),
        (2,8),
        (1,),
        (2,-1),
        (2,2),
        (2,1),
        (1,),
        (2,17),
        (2,-9),
        (2,1),
        (2,1),
        (2,-3),
        (2,11),
        (1,),
        (1,),
        (2,1),
        (1,),
        (2,1),
        (1,),
        (1,),
        (2,-13),
        (2,-19),
        (2,1),
        (2,3),
        (2,26),
        (2,-30),
        (2,12),
        (2,-1),
        (2,3),
        (2,1),
        (1,),
        (1,),
        (1,),
        (2,-9),
        (2,18),
        (2,1),
        (2,2),
        (1,),
        (1,),
        (2,9),
        (1,),
        (1,),
        (1,),
        (2,-1),
        (2,2),
        (2,-37),
        (2,1),
        (2,3),
        (1,),
        (2,15),
        (2,-21),
        (2,22),
        (2,-6),
        (2,1),
        (1,),
        (2,2),
        (2,1),
        (1,),
        (2,-10),
        (1,),
        (1,),
        (2,20),
        (2,1),
        (2,2),
        (2,2),
        (2,-6),
        (2,-11),
        (1,),
        (1,),
        (1,),
    )

def test_get_cycles(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    cycles = subject.get_cycles(data)
    assert cycles[20] == 21
    assert cycles[60] == 19
    assert cycles[100] == 18
    assert cycles[140] == 21
    assert cycles[180] == 16
    assert cycles[220] == 18

def test_signal_strength(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.signal_strength(data) == 13140

def test_draw(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.draw(data) == "██  ██  ██  ██  ██  ██  ██  ██  ██  ██  \n███   ███   ███   ███   ███   ███   ███ \n████    ████    ████    ████    ████    \n█████     █████     █████     █████     \n██████      ██████      ██████      ████\n███████       ███████       ███████     "

