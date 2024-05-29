"""
Solution for day 09 of year 2016
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read().strip()


def decompress(data):
    result = ''
    match = regex.search(r'\(([0-9]+)x([0-9]+)\)',data)
    while match != None:
        result += data[:match.span()[0]] + (data[match.span()[1]:match.span()[1] + int(match.groups()[0])] * int(match.groups()[1]))
        data = data[match.span()[1] + int(match.groups()[0]):]
        match = regex.search(r'\(([0-9]+)x([0-9]+)\)',data)
    result += data
    return result

def decompress2(data):
    result = 0
    match = regex.search(r'\(([0-9]+)x([0-9]+)\)',data)
    while match != None:
        result += len(data[:match.span()[0]])
        result += decompress2(data[match.span()[1]:match.span()[1] + int(match.groups()[0])]) * int(match.groups()[1])
        data = data[match.span()[1] + int(match.groups()[0]):]
        match = regex.search(r'\(([0-9]+)x([0-9]+)\)',data)
    result += len(data)
    return result

def parse_lines(lines):
    return [x for x in lines]

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = len(decompress(data))

    # Part 2
    solution2 =  decompress2(data)
    print(solution2)
    exit()
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
