import solve_2016_17 as subject
import pytest


def test_find_path():
    assert subject.find_path('ihgpwlah') == 'DDRRRD'
    assert subject.find_path('kglvqrro') == 'DDUDRLRRUDRD'
    assert subject.find_path('ulqzkmiv') == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'
    assert subject.find_path('ihgpwlah', True) == 370
    assert subject.find_path('kglvqrro', True) == 492
    assert subject.find_path('ulqzkmiv', True) == 830


