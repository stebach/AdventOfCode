"""
Solution for day 06 of year 2020
"""

import os
from functools import reduce

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    data = []
    current_group = []
    lines += ['']
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            data.append(tuple(current_group))
            current_group = []
        else:
            current_group.append(line)
    return tuple(data)

def unique_answers(answers):
    return list(reduce(lambda a,b: set(a).union(set(b)), [[*x] for x in answers]))

def same_answers(answers):
    return list(reduce(lambda a,b: set(a) & set(b), [[*x] for x in answers]))

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum([len(unique_answers(x)) for x in data])

    # Part 2
    solution2 = sum([len(same_answers(x)) for x in data])

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
