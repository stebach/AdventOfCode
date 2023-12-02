"""
Solution for day 02 of year 2023
"""

import os
import regex
import math

def process_draw(draw):
    data = regex.split(",? ", draw)
    return [int(data[data.index(x)-1]) if x in data else 0 for x in ['red','green','blue']]

def process_line(line):
    line = regex.split('[;:] ', line.strip()[5:])
    game = int(line[0])
    data = [process_draw(x) for x in line[1:]]
    return tuple([game, data])

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(process_line, inputdata.readlines()))

def part1(data, red=12, green=13, blue=14):
    """Solve part 1"""
    return sum([x[0] if sum([1 if y[0] <= red and y[1] <= green and y[2] <= blue else 0 for y in x[1]]) == len(x[1]) else 0 for x in data])

def part2(data):
    """Solve part 2"""
    return sum([math.prod([max([y[z] for y in x[1]]) for z in range(3)]) for x in data])

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
