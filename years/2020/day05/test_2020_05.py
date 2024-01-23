import solve_2020_05 as subject
import pytest


def test_decode_seat():
    assert subject.decode_seat('FBFBBFFRLR') == (44,5,357)
    assert subject.decode_seat('BFFFBBFRRR') == (70,7,567)
    assert subject.decode_seat('FFFBBBFRRR') == (14,7,119)
    assert subject.decode_seat('BBFFBBFRLL') == (102,4,820)

