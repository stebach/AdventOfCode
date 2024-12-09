import solve_2024_09 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return '2333133121414131402'

def test_get_blocks(puzzle_input):
    assert subject.get_blocks(puzzle_input) == [
        {
            'type': 'block',
            'id': 0,
            'amount': 2,
        },
        {
            'type': 'empty',
            'amount': 3,
        },
        {
            'type': 'block',
            'id': 1,
            'amount': 3,
        },
        {
            'type': 'empty',
            'amount': 3,
        },
        {
            'type': 'block',
            'id': 2,
            'amount': 1,
        },
        {
            'type': 'empty',
            'amount': 3,
        },
        {
            'type': 'block',
            'id': 3,
            'amount': 3,
        },
        {
            'type': 'empty',
            'amount': 1,
        },
        {
            'type': 'block',
            'id': 4,
            'amount': 2,
        },
        {
            'type': 'empty',
            'amount': 1,
        },
        {
            'type': 'block',
            'id': 5,
            'amount': 4,
        },
        {
            'type': 'empty',
            'amount': 1,
        },
        {
            'type': 'block',
            'id': 6,
            'amount': 4,
        },
        {
            'type': 'empty',
            'amount': 1,
        },
        {
            'type': 'block',
            'id': 7,
            'amount': 3,
        },
        {
            'type': 'empty',
            'amount': 1,
        },
        {
            'type': 'block',
            'id': 8,
            'amount': 4,
        },
        {
            'type': 'block',
            'id': 9,
            'amount': 2,
        },
    ]

def test_move_blocks(puzzle_input):
    assert subject.move_blocks(subject.get_blocks(puzzle_input)) == [
        {
            'type': 'block',
            'id': 0,
            'amount': 2,
        },
        {
            'type': 'block',
            'id': 9,
            'amount': 2,
        },
        {
            'type': 'block',
            'id': 8,
            'amount': 1,
        },
        {
            'type': 'block',
            'id': 1,
            'amount': 3,
        },
        {
            'type': 'block',
            'id': 8,
            'amount': 3,
        },
        {
            'type': 'block',
            'id': 2,
            'amount': 1,
        },
        {
            'type': 'block',
            'id': 7,
            'amount': 3,
        },
        {
            'type': 'block',
            'id': 3,
            'amount': 3,
        },
        {
            'type': 'block',
            'id': 6,
            'amount': 1,
        },
        {
            'type': 'block',
            'id': 4,
            'amount': 2,
        },
        {
            'type': 'block',
            'id': 6,
            'amount': 1,
        },
        {
            'type': 'block',
            'id': 5,
            'amount': 4,
        },
        {
            'type': 'block',
            'id': 6,
            'amount': 2,
        },
        {
            'type': 'empty',
            'amount': 14,
        },
    ]
def test_move_blocks_whole_files(puzzle_input):
    assert subject.move_blocks_whole_files(subject.get_blocks(puzzle_input)) == [
        {
            'type': 'block',
            'id': 0,
            'amount': 2,
        },
        {
            'type': 'block',
            'id': 9,
            'amount': 2,
        },
        {
            'type': 'block',
            'id': 2,
            'amount': 1,
        },
        {
            'type': 'block',
            'id': 1,
            'amount': 3,
        },
        {
            'type': 'block',
            'id': 7,
            'amount': 3,
        },
        {
            'type': 'empty',
            'amount': 1,
        },
        {
            'type': 'block',
            'id': 4,
            'amount': 2,
        },
        {
            'type': 'empty',
            'amount': 1,
        },
        {
            'type': 'block',
            'id': 3,
            'amount': 3,
        },
        {
            'type': 'empty',
            'amount': 4,
        },
        {
            'type': 'block',
            'id': 5,
            'amount': 4,
        },
        {
            'type': 'empty',
            'amount': 1,
        },
        {
            'type': 'block',
            'id': 6,
            'amount': 4,
        },
        {
            'type': 'empty',
            'amount': 5,
        },
        {
            'type': 'block',
            'id': 8,
            'amount': 4,
        },
        {
            'type': 'empty',
            'amount': 2,
        },
    ]

def test_checksum(puzzle_input):
    assert subject.checksum(subject.move_blocks(subject.get_blocks(puzzle_input))) == 1928
    assert subject.checksum(subject.move_blocks_whole_files(subject.get_blocks(puzzle_input))) == 2858



def test_solve(puzzle_input):
    assert subject.solve(puzzle_input) == (1928, 2858)

