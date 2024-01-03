"""
Solution for day 02 of year 2019
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return [int(x) for x in inputdata.read().split(',')]

def parse_line(line):
    return line.strip()

def parse_lines(lines):
    return [x for x in lines]

def intcode(data):
    pointer = 0
    while data[pointer] != 99:
        if data[pointer] == 1:
            data[data[pointer+3]] = data[data[pointer+1]] + data[data[pointer+2]]
            pointer += 4
        elif data[pointer] == 2:
            data[data[pointer+3]] = data[data[pointer+1]] * data[data[pointer+2]]
            pointer += 4
        else:
            print("ERR: UNKNOWN OPCODE: " + str(data[pointer]))
            exit()
    return data

def part1(data):
    """Solve part 1"""
    data2 = deepcopy(data)
    data2[1] = 12
    data2[2] = 2

    data2 = intcode(data2)
    return data2[0]

def part2(data):
    """Solve part 2"""
    for noun in range(100):
        for verb in range(100):
            data2 = deepcopy(data)
            data2[1] = noun
            data2[2] = verb
            data2 = intcode(data2)
            if data2[0] == 19690720:
                return noun * 100 + verb
    return 0


def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
