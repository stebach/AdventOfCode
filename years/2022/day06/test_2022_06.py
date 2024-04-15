import solve_2022_06 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

@pytest.fixture
def puzzle_input2():
    return "bvwbjplbgvbhsrlpgdmjqwftvncz"

@pytest.fixture
def puzzle_input3():
    return "nppdvjthqldpwncqszvftbrmjlhg"

@pytest.fixture
def puzzle_input4():
    return "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

@pytest.fixture
def puzzle_input5():
    return "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def test_find_marker(puzzle_input, puzzle_input2, puzzle_input3, puzzle_input4, puzzle_input5):
    assert subject.find_marker(puzzle_input) == 7
    assert subject.find_marker(puzzle_input2) == 5
    assert subject.find_marker(puzzle_input3) == 6
    assert subject.find_marker(puzzle_input4) == 10
    assert subject.find_marker(puzzle_input5) == 11

    assert subject.find_marker(puzzle_input, 14) == 19
    assert subject.find_marker(puzzle_input2, 14) == 23
    assert subject.find_marker(puzzle_input3, 14) == 23
    assert subject.find_marker(puzzle_input4, 14) == 29
    assert subject.find_marker(puzzle_input5, 14) == 26

