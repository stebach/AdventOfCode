import solve_2020_07 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'light red bags contain 1 bright white bag, 2 muted yellow bags.',
        'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
        'bright white bags contain 1 shiny gold bag.',
        'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
        'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
        'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
        'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
        'faded blue bags contain no other bags.',
        'dotted black bags contain no other bags.'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        'shiny gold bags contain 2 dark red bags.',
        'dark red bags contain 2 dark orange bags.',
        'dark orange bags contain 2 dark yellow bags.',
        'dark yellow bags contain 2 dark green bags.',
        'dark green bags contain 2 dark blue bags.',
        'dark blue bags contain 2 dark violet bags.',
        'dark violet bags contain no other bags.'
    ]

def test_parse_line(puzzle_input):
    assert dict(map(subject.parse_line, puzzle_input)) == {
        'light red': (
            ('bright white',1),
            ('muted yellow',2)
        ),
        'dark orange': (
            ('bright white',3),
            ('muted yellow',4),
        ),
        'bright white': (
            ('shiny gold',1),
        ),
        'muted yellow': (
            ('shiny gold',2),
            ('faded blue',9),
        ),
        'shiny gold': (
            ('dark olive',1),
            ('vibrant plum',2),
        ),
        'dark olive': (
            ('faded blue',3),
            ('dotted black',4),
        ),
        'vibrant plum': (
            ('faded blue',5),
            ('dotted black',6),
        ),
        'faded blue': tuple(
        ),
        'dotted black': tuple(
        ),
    }

def test_contains_bag(puzzle_input):
    data = dict(map(subject.parse_line, puzzle_input))
    assert subject.contains_bag(data, 'bright white', 'shiny gold') == True
    assert subject.contains_bag(data, 'muted yellow', 'shiny gold') == True
    assert subject.contains_bag(data, 'dark orange', 'shiny gold') == True
    assert subject.contains_bag(data, 'light red', 'shiny gold') == True
    assert subject.contains_bag(data, 'shiny gold', 'shiny gold') == False
    assert subject.contains_bag(data, 'dark olive', 'shiny gold') == False
    assert subject.contains_bag(data, 'vibrant plum', 'shiny gold') == False
    assert subject.contains_bag(data, 'faded blue', 'shiny gold') == False
    assert subject.contains_bag(data, 'dotted black', 'shiny gold') == False

def test_count_bags(puzzle_input, puzzle_input2):
    assert subject.count_bags(dict(map(subject.parse_line, puzzle_input)), 'shiny gold') - 1 == 32
    assert subject.count_bags(dict(map(subject.parse_line, puzzle_input2)), 'shiny gold') - 1 == 126

