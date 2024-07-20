import solve_2017_09 as subject
import pytest

def test_parse():
    assert subject.parse('{{<a>},{<{!>}>},{<<<<>},{<!!!>>}}') == {
        'score': 1,
        'total_score': 9,
        'garbage': [
        ],
        'garbageCount': 6,
        'groups': [
            {
                'score': 2,
                'total_score': 2,
                'garbage': [
                    'a',
                ],
                'garbageCount': 1,
                'groups': [],
            },
            {
                'score': 2,
                'total_score': 2,
                'garbage': [
                    '{!>}',
                ],
                'garbageCount': 2,
                'groups': [],
            },
            {
                'score': 2,
                'total_score': 2,
                'garbage': [
                    '<<<',
                ],
                'garbageCount': 3,
                'groups': [],
            },
            {
                'score': 2,
                'total_score': 2,
                'garbage': [
                    '!!!>',
                ],
                'garbageCount': 0,
                'groups': [],
            }
        ]
    }

def test_get_score():
    assert subject.get_score('{}') == 1
    assert subject.get_score('{{{}}}') == 6
    assert subject.get_score('{{},{}}') == 5
    assert subject.get_score('{{{},{},{{}}}}') == 16
    assert subject.get_score('{<a>,<a>,<a>,<a>}') == 1
    assert subject.get_score('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
    assert subject.get_score('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
    assert subject.get_score('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3


