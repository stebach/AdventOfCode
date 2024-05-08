import solve_2015_12 as subject
import pytest

def test_get_sum():
    assert subject.get_sum('[1,2,3]') == 6
    assert subject.get_sum('{"a":2,"b":4}') == 6
    assert subject.get_sum('[[[3]]]') == 3
    assert subject.get_sum('{"a":{"b":4},"c":-1}') == 3
    assert subject.get_sum('{"a":[-1,1]}') == 0
    assert subject.get_sum('[-1,{"a":1}]') == 0
    assert subject.get_sum('[]') == 0
    assert subject.get_sum('{}') == 0

    assert subject.get_sum('[1,2,3]', 'red') == 6
    assert subject.get_sum('[1,{"c":"red","b":2},3]', 'red') == 4
    assert subject.get_sum('{"d":"red","e":[1,2,3,4],"f":5}', 'red') == 0
    assert subject.get_sum('[1,"red",5]', 'red') == 6


