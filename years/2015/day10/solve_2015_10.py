"""
Solution for day 10 of year 2015
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read().strip()

def look_and_say(data, times):
    data = str(data)
    for i in range(times):
        result = regex.findall(r'(([0-9])\2*)',data)
        data = "".join([str(len(x[0])) + x[1] for x in result])
    return data

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = len(look_and_say(data, 40))

    # Part 2
    solution2 =  len(look_and_say(data, 50))
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

