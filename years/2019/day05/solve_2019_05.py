"""
Solution for day 05 of year 2019
"""

import os
from math import floor
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return [int(x) for x in inputdata.read().split(',')]

def intcode(data, input = [], output = []):
    pointer = 0
    while data[pointer] != 99:
        opcode = data[pointer] % 100
        if opcode == 1:
            data[data[pointer+3]] = intcode_get_param(1,data,pointer) + intcode_get_param(2,data,pointer)
            pointer += 4
        elif opcode == 2:
            data[data[pointer+3]] = intcode_get_param(1,data,pointer) * intcode_get_param(2,data,pointer)
            pointer += 4
        elif opcode == 3:
            data[data[pointer+1]] = input.pop(0)
            pointer += 2
        elif opcode == 4:
            output.append(intcode_get_param(1,data,pointer))
            pointer += 2
        elif opcode == 5:
            if intcode_get_param(1,data,pointer) != 0:
                pointer = intcode_get_param(2,data,pointer)
            else:
                pointer += 3
        elif opcode == 6:
            if intcode_get_param(1,data,pointer) == 0:
                pointer = intcode_get_param(2,data,pointer)
            else:
                pointer += 3
        elif opcode == 7:
            if intcode_get_param(1,data,pointer) < intcode_get_param(2,data,pointer):
                data[data[pointer+3]] = 1
            else:
                data[data[pointer+3]] = 0
            pointer += 4
        elif opcode == 8:
            if intcode_get_param(1,data,pointer) == intcode_get_param(2,data,pointer):
                data[data[pointer+3]] = 1
            else:
                data[data[pointer+3]] = 0
            pointer += 4
        else:
            print (data)
            print("ERR: UNKNOWN OPCODE: " + str(data[pointer]))
            exit()
    return data

def intcode_get_param(no, data, pointer):
    mode = 0
    if data[pointer] >= pow(10,1+no):
        tostr = str(data[pointer])
        mode = int(tostr[len(tostr)-2-no])
    if mode == 0:
        return data[data[pointer+no]]
    else:
        return data[pointer+no]

def part1(data):
    """Solve part 1"""
    input = [1]
    output = []
    data2 = deepcopy(data)
    intcode(data2, input, output)
    return output[-1]

def part2(data):
    """Solve part 2"""
    input = [5]
    output = []
    data2 = deepcopy(data)
    intcode(data2, input, output)
    return output[-1]


def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

