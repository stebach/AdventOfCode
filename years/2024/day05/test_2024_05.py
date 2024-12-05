import solve_2024_05 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '47|53',
        '97|13',
        '97|61',
        '97|47',
        '75|29',
        '61|13',
        '75|53',
        '29|13',
        '97|29',
        '53|29',
        '61|53',
        '97|53',
        '61|29',
        '47|13',
        '75|47',
        '97|75',
        '47|61',
        '75|61',
        '47|29',
        '75|13',
        '53|13',
        '',
        '75,47,61,53,29',
        '97,61,53,29,13',
        '75,29,13',
        '75,97,47,61,53',
        '61,13,29',
        '97,13,75,29,47'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'rules': {
            47: [53, 13, 61, 29],
            97: [13, 61, 47, 29, 53, 75],
            75: [29, 53, 47, 61, 13],
            61: [13, 53, 29],
            29: [13],
            53: [29, 13],
        },
        'pages': [
            [75, 47, 61, 53, 29],
            [97, 61, 53, 29, 13],
            [75, 29, 13],
            [75, 97, 47, 61, 53],
            [61, 13, 29],
            [97, 13, 75, 29, 47]
        ]
    }

def test_right_order(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.right_order(data['pages'][0], data['rules']) == True
    assert subject.right_order(data['pages'][1], data['rules']) == True
    assert subject.right_order(data['pages'][2], data['rules']) == True
    assert subject.right_order(data['pages'][3], data['rules']) == False
    assert subject.right_order(data['pages'][4], data['rules']) == False
    assert subject.right_order(data['pages'][5], data['rules']) == False

def test_get_sum_of_middle_page_numbers(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.get_sum_of_middle_page_numbers(
        [x for x in data['pages'] if subject.right_order(x, data['rules'])]
    ) == 143
    assert subject.get_sum_of_middle_page_numbers(
        [subject.order(x, data['rules']) for x in data['pages'] if not subject.right_order(x, data['rules'])]
    ) == 123

def test_order(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.order(data['pages'][3], data['rules']) == [97,75,47,61,53]
    assert subject.order(data['pages'][4], data['rules']) == [61,29,13]
    assert subject.order(data['pages'][5], data['rules']) == [97,75,47,29,13]

def test_solve(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.solve(data) == (143,123)

