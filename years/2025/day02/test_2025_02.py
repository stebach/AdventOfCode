import solve_2025_02 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ['11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124']

def test_parse_line(puzzle_input):
    assert tuple(subject.parse_line(puzzle_input)) == (
        (11,22),
        (95,115),
        (998,1012),
        (1188511880,1188511890),
        (222220,222224),
        (1698522,1698528),
        (446443,446449),
        (38593856,38593862),
        (565653,565659),
        (824824821,824824827),
        (2121212118,2121212124)
    )


def test_solve(puzzle_input):
    data = tuple(subject.parse_line(puzzle_input))
    assert subject.solve(data) == (1227775554,4174379265)

