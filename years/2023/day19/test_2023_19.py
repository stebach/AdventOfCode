import solve_2023_19 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'px{a<2006:qkq,m>2090:A,rfg}',
        'pv{a>1716:R,A}',
        'lnx{m>1548:A,A}',
        'rfg{s<537:gd,x>2440:R,A}',
        'qs{s>3448:A,lnx}',
        'qkq{x<1416:A,crn}',
        'crn{x>2662:A,R}',
        'in{s<1351:px,qqz}',
        'qqz{s>2770:qs,m<1801:hdj,R}',
        'gd{a>3333:R,R}',
        'hdj{m>838:A,pv}',
        '',
        '{x=787,m=2655,a=1222,s=2876}',
        '{x=1679,m=44,a=2067,s=496}',
        '{x=2036,m=264,a=79,s=2244}',
        '{x=2461,m=1339,a=466,s=291}',
        '{x=2127,m=1623,a=2188,s=1013}'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        {
            'px':(('a','<',2006,'qkq'),('m','>',2090,'A'),('rfg')),
            'pv':(('a','>',1716,'R'),('A')),
            'lnx':(('m','>',1548,'A'),('A')),
            'rfg':(('s','<',537,'gd'),('x','>',2440,'R'),('A')),
            'qs':(('s','>',3448,'A'),('lnx')),
            'qkq':(('x','<',1416,'A'),('crn')),
            'crn':(('x','>',2662,'A'),('R')),
            'in':(('s','<',1351,'px'),('qqz')),
            'qqz':(('s','>',2770,'qs'),('m','<',1801,'hdj'),('R')),
            'gd':(('a','>',3333,'R'),('R')),
            'hdj':(('m','>',838,'A'),('pv')),
        },
        (
            (787,2655,1222,2876),
            (1679,44,2067,496),
            (2036,264,79,2244),
            (2461,1339,466,291),
            (2127,1623,2188,1013)
        )
    )

def test_part1_example1(puzzle_input):
    assert subject.part1(subject.parse_lines(puzzle_input)) == 19114

def test_part2_example1(puzzle_input):
    assert subject.part2(subject.parse_lines(puzzle_input)) == 167409079868000

