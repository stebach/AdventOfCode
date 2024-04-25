import solve_2022_16 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB",
        "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
        "Valve CC has flow rate=2; tunnels lead to valves DD, BB",
        "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
        "Valve EE has flow rate=3; tunnels lead to valves FF, DD",
        "Valve FF has flow rate=0; tunnels lead to valves EE, GG",
        "Valve GG has flow rate=0; tunnels lead to valves FF, HH",
        "Valve HH has flow rate=22; tunnel leads to valve GG",
        "Valve II has flow rate=0; tunnels lead to valves AA, JJ",
        "Valve JJ has flow rate=21; tunnel leads to valve II",
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'AA': (0, ('DD', 'II', 'BB')),
        'BB': (13, ('CC', 'AA')),
        'CC': (2, ('DD', 'BB')),
        'DD': (20, ('CC', 'AA', 'EE')),
        'EE': (3, ('FF', 'DD')),
        'FF': (0, ('EE', 'GG')),
        'GG': (0, ('FF', 'HH')),
        'HH': (22, ('GG',)),
        'II': (0, ('AA', 'JJ')),
        'JJ': (21, ('II',)),
    }

def test_release_preassure(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.release_preassure(data, 30) == 1651

def test_release_preassure2(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.release_preassure2(data, 26) == 1707
