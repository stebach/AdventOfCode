"""
Solution for day 01 of year 2024
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    list1 = []
    list2 = []

    for line in lines:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

    return [list1, list2]

def get_distances_ordered(data):
    copydata = deepcopy(data)
    copydata[0].sort()
    copydata[1].sort()
    return sum(abs(a-b) for a, b in zip(*copydata))

def get_similarity_score(data):
    return sum([data[1].count(x) * x for x in data[0]])

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_distances_ordered(data)
    # Part 2
    solution2 = get_similarity_score(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

