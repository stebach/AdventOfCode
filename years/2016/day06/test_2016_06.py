import solve_2016_06 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return (
        'eedadn',
        'drvtee',
        'eandsr',
        'raavrd',
        'atevrs',
        'tsrnev',
        'sdttsa',
        'rasrtv',
        'nssdts',
        'ntnada',
        'svetve',
        'tesnvt',
        'vntsnd',
        'vrdear',
        'dvrsen',
        'enarar'
    )

def test_error_correct(puzzle_input):
    assert subject.error_correct(puzzle_input) == 'easter'
    assert subject.error_correct(puzzle_input, True) == 'advent'

