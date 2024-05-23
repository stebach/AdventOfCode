import solve_2016_04 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'aaaaa-bbb-z-y-x-123[abxyz]',
        'a-b-c-d-e-f-g-h-987[abcde]',
        'not-a-real-room-404[oarel]',
        'totally-real-room-200[decoy]',
        'qzmt-zixmtkozy-ivhz-343[zimth]',
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('aaaaa-bbb-z-y-x', 123, 'abxyz'),
        ('a-b-c-d-e-f-g-h', 987, 'abcde'),
        ('not-a-real-room', 404, 'oarel'),
        ('totally-real-room', 200, 'decoy'),
        ('qzmt-zixmtkozy-ivhz', 343, 'zimth'),

    )

def test_is_real_room(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.is_real_room(data[0]) == True
    assert subject.is_real_room(data[1]) == True
    assert subject.is_real_room(data[2]) == True
    assert subject.is_real_room(data[3]) == False
    assert subject.is_real_room(data[4]) == True

def test_decrypt(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.decrypt(data[4]) == 'very encrypted name'

