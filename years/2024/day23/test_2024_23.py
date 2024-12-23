import solve_2024_23 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'kh-tc',
        'qp-kh',
        'de-cg',
        'ka-co',
        'yn-aq',
        'qp-ub',
        'cg-tb',
        'vc-aq',
        'tb-ka',
        'wh-tc',
        'yn-cg',
        'kh-ub',
        'ta-co',
        'de-co',
        'tc-td',
        'tb-wq',
        'wh-td',
        'ta-ka',
        'td-qp',
        'aq-cg',
        'wq-ub',
        'ub-vc',
        'de-ta',
        'wq-aq',
        'wq-vc',
        'wh-yn',
        'ka-de',
        'kh-ta',
        'co-tc',
        'wh-qp',
        'tb-vc',
        'td-yn'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('kh', 'tc'),
        ('qp', 'kh'),
        ('de', 'cg'),
        ('ka', 'co'),
        ('yn', 'aq'),
        ('qp', 'ub'),
        ('cg', 'tb'),
        ('vc', 'aq'),
        ('tb', 'ka'),
        ('wh', 'tc'),
        ('yn', 'cg'),
        ('kh', 'ub'),
        ('ta', 'co'),
        ('de', 'co'),
        ('tc', 'td'),
        ('tb', 'wq'),
        ('wh', 'td'),
        ('ta', 'ka'),
        ('td', 'qp'),
        ('aq', 'cg'),
        ('wq', 'ub'),
        ('ub', 'vc'),
        ('de', 'ta'),
        ('wq', 'aq'),
        ('wq', 'vc'),
        ('wh', 'yn'),
        ('ka', 'de'),
        ('kh', 'ta'),
        ('co', 'tc'),
        ('wh', 'qp'),
        ('tb', 'vc'),
        ('td', 'yn')
    )

def test_find_interconnected_starting_with_t(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.find_interconnected_starting_with_t(data) == 7

def test_find_largest_set(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.find_largest_set(data) == 'co,de,ka,ta'

def test_solve(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.solve(data) == (7, 'co,de,ka,ta')

