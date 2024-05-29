import solve_2016_09 as subject
import pytest

def test_decompress():
    assert subject.decompress('ADVENT') == 'ADVENT'
    assert subject.decompress('A(1x5)BC') == 'ABBBBBC'
    assert subject.decompress('(3x3)XYZ') == 'XYZXYZXYZ'
    assert subject.decompress('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG'
    assert subject.decompress('(6x1)(1x3)A') == '(1x3)A'
    assert subject.decompress('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY'

def test_decompress2():
    assert subject.decompress2('(3x3)XYZ') == 9
    assert subject.decompress2('X(8x2)(3x3)ABCY') == 20
    assert subject.decompress2('(27x12)(20x12)(13x14)(7x10)(1x12)A') == 241920
    assert subject.decompress2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') == 445
    


