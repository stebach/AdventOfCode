import solve_2018_14 as subject
import pytest

def test_part1_example1():
    assert subject.make_recipes([3,7],9) == 5158916779
    assert subject.make_recipes([3,7],5) == 124515891
    assert subject.make_recipes([3,7],18) == 9251071085
    assert subject.make_recipes([3,7],2018) == 5941429882


def test_part2_example1():
    assert subject.search_in_recipes('51589', [3,7]) == 9
    assert subject.search_in_recipes('01245', [3,7]) == 5
    assert subject.search_in_recipes('92510', [3,7]) == 18
    assert subject.search_in_recipes('59414', [3,7]) == 2018
