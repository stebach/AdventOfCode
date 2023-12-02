import solve_2022_02 as subject

def test_part1_example1():
    puzzle_input = tuple(map(subject.process_line, ["A Y","B X","C Z"]))
    assert subject.part1(puzzle_input) == 15

def test_part2_example1():
    puzzle_input = tuple(map(subject.process_line, ["A Y","B X","C Z"]))
    assert subject.part2(puzzle_input) == 12

