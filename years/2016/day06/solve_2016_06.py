"""
Solution for day 06 of year 2016
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def error_correct(data, use_least_occurring = False):
    return "".join([most_occurring_char([y[x] for y in data], use_least_occurring) for x in range(len(data[0]))])

def most_occurring_char(arr, use_least_occurring):
    occurences = {}
    most = 0
    most_char = ''
    if use_least_occurring:
        most = len(arr) + 1
    for x in arr:
        if x not in occurences:
            occurences[x] = arr.count(x)
            if not use_least_occurring and occurences[x] > most:
                most = occurences[x]
                most_char = x
            elif use_least_occurring and occurences[x] < most:
                most = occurences[x]
                most_char = x
    return most_char

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = error_correct(data)

    # Part 2
    solution2 = error_correct(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
