"""
Solution for day 05 of year 2018
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read()

def reduce(string):
    list = [ord(string[x]) for x in range(len(string))]
    unique = set(list)
    to_remove = [chr(x) + chr(x + 32) + "|" + chr(x + 32) + chr(x)  for x in unique if x < 97]
    length = len(string)
    repeat = True
    while repeat:
        string = regex.sub("|".join(to_remove), "", string)
        repeat = length != len(string)
        length = len(string)

    return string

def parse_line(line):
    return line.strip()

def part1(data):
    """Solve part 1"""
    return len(reduce(data))

def part2(data):
    """Solve part 2"""
    list = [ord(data[x]) for x in range(len(data))]
    unique = set(list)
    to_remove = [chr(x) + "|" + chr(x + 32) for x in unique if x < 97]
    results = []
    for run in to_remove:
        results = results + [len(reduce(regex.sub(run,"",data)))]

    return min(results)

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
