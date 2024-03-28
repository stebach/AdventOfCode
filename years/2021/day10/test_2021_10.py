import solve_2021_10 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]"
    ]

def test_get_corrupted_score(puzzle_input):
    assert subject.get_corrupted_score(puzzle_input) == 26397

def test_get_incomplete_score(puzzle_input):
    assert subject.get_incomplete_score(puzzle_input) == 288957

def test_analyze(puzzle_input):
    assert subject.analyze(puzzle_input[0]) == ('i', ['}','}',']',']',')','}',')',']'])
    assert subject.analyze(puzzle_input[1]) == ('i', [')','}','>',']','}',')'])
    assert subject.analyze(puzzle_input[2]) == ('c', '}')
    assert subject.analyze(puzzle_input[3]) == ('i',['}','}','>','}','>',')',')',')',')'])
    assert subject.analyze(puzzle_input[4]) == ('c',')')
    assert subject.analyze(puzzle_input[5]) == ('c',']')
