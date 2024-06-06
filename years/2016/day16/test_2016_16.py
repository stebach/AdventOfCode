import solve_2016_16 as subject
import pytest

def test_dragon_curve():
    assert subject.dragon_curve("1") == "100"
    assert subject.dragon_curve("0") == "001"
    assert subject.dragon_curve("11111") == "11111000000"
    assert subject.dragon_curve("111100001010") == "1111000010100101011110000"


def test_checksum():
    assert subject.checksum("110010110100", 12) == "100"

def test_checksum_for_disk():
    assert subject.checksum_for_disk("10000", 20) == "01100"

