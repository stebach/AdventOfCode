import solve_2021_11 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "5483143223",
        "2745854711",
        "5264556173",
        "6141336146",
        "6357385478",
        "4167524645",
        "2176841721",
        "6882881134",
        "4846848554",
        "5283751526"
    ]

def test_parse_line(puzzle_input):
    assert list(map(subject.parse_line, puzzle_input)) == [
        [5,4,8,3,1,4,3,2,2,3],
        [2,7,4,5,8,5,4,7,1,1],
        [5,2,6,4,5,5,6,1,7,3],
        [6,1,4,1,3,3,6,1,4,6],
        [6,3,5,7,3,8,5,4,7,8],
        [4,1,6,7,5,2,4,6,4,5],
        [2,1,7,6,8,4,1,7,2,1],
        [6,8,8,2,8,8,1,1,3,4],
        [4,8,4,6,8,4,8,5,5,4],
        [5,2,8,3,7,5,1,5,2,6]
    ]

def test_step(puzzle_input):
    data = list(map(subject.parse_line, puzzle_input))
    new_data = subject.step(data)
    assert new_data['map'] == [
        [6,5,9,4,2,5,4,3,3,4],
        [3,8,5,6,9,6,5,8,2,2],
        [6,3,7,5,6,6,7,2,8,4],
        [7,2,5,2,4,4,7,2,5,7],
        [7,4,6,8,4,9,6,5,8,9],
        [5,2,7,8,6,3,5,7,5,6],
        [3,2,8,7,9,5,2,8,3,2],
        [7,9,9,3,9,9,2,2,4,5],
        [5,9,5,7,9,5,9,6,6,5],
        [6,3,9,4,8,6,2,6,3,7]
    ]
    assert new_data['flashes'] == 0

    new_data = subject.step(new_data['map'])
    assert new_data['map'] == [
        [8,8,0,7,4,7,6,5,5,5],
        [5,0,8,9,0,8,7,0,5,4],
        [8,5,9,7,8,8,9,6,0,8],
        [8,4,8,5,7,6,9,6,0,0],
        [8,7,0,0,9,0,8,8,0,0],
        [6,6,0,0,0,8,8,9,8,9],
        [6,8,0,0,0,0,5,9,4,3],
        [0,0,0,0,0,0,7,4,5,6],
        [9,0,0,0,0,0,0,8,7,6],
        [8,7,0,0,0,0,6,8,4,8]
    ]
    assert new_data['flashes'] == 35

    new_data = subject.step(new_data['map'])
    assert new_data['map'] == [
        [0,0,5,0,9,0,0,8,6,6],
        [8,5,0,0,8,0,0,5,7,5],
        [9,9,0,0,0,0,0,0,3,9],
        [9,7,0,0,0,0,0,0,4,1],
        [9,9,3,5,0,8,0,0,6,3],
        [7,7,1,2,3,0,0,0,0,0],
        [7,9,1,1,2,5,0,0,0,9],
        [2,2,1,1,1,3,0,0,0,0],
        [0,4,2,1,1,2,5,0,0,0],
        [0,0,2,1,1,1,9,0,0,0]
    ]
    assert new_data['flashes'] == 45

    new_data = subject.step(new_data['map'])
    new_data = subject.step(new_data['map'])
    new_data = subject.step(new_data['map'])
    new_data = subject.step(new_data['map'])
    new_data = subject.step(new_data['map'])
    new_data = subject.step(new_data['map'])
    new_data = subject.step(new_data['map'])
    assert new_data['map'] == [
        [0,4,8,1,1,1,2,9,7,6],
        [0,0,3,1,1,1,2,0,0,9],
        [0,0,4,1,1,1,2,5,0,4],
        [0,0,8,1,1,1,1,4,0,6],
        [0,0,9,9,1,1,1,3,0,6],
        [0,0,9,3,5,1,1,2,3,3],
        [0,4,4,2,3,6,1,1,3,0],
        [5,5,3,2,2,5,2,3,5,0],
        [0,5,3,2,2,5,0,6,0,0],
        [0,0,3,2,2,4,0,0,0,0]
    ]
    assert new_data['flashes'] == 29

def test_count_flashes(puzzle_input):
    data = list(map(subject.parse_line, puzzle_input))
    assert subject.count_flashes(data, 100) == 1656

def test_steps_for_full_flash(puzzle_input):
    data = list(map(subject.parse_line, puzzle_input))
    assert subject.steps_for_full_flash(data) == 195


