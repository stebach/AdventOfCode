"""
Solution for day 03 of year 2021
"""

import os
import math
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:

        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()
    return int(line,2)

def get_power_consumption(data):
    maxnum = max(data)
    check = int(int("1" + bin(maxnum)[2:].replace("1","0"),2) / 2)
    mask = int(check * 2 - 1)

    gamma = 0

    threshold = len(data) / 2

    while check > 0:
        if sum([(x & check) > 0 for x in data]) > threshold:
            gamma |= check
        check = math.floor(check/2)

    epsilon = gamma ^ mask
    return gamma * epsilon

def get_oxygen_generator_rating(data):
    oxygen = filter_list(data)
    co2 = filter_list(data, True)
    return oxygen * co2

def filter_list(data, prioritize_fewest=False):
    localdata = deepcopy(data)
    maxnum = max(data)
    check = int(int("1" + bin(maxnum)[2:].replace("1","0"),2) / 2)
    while check > 0 and len(localdata) > 1:
        amount = sum([(x & check) > 0 for x in localdata])
        if amount >= len(localdata)/2:
            if prioritize_fewest:
                localdata = [x for x in localdata if x & check == 0]
            else:
                localdata = [x for x in localdata if x & check > 0]
        else:
            if prioritize_fewest:
                localdata = [x for x in localdata if x & check > 0]
            else:
                localdata = [x for x in localdata if x & check == 0]
        check = math.floor(check/2)

    return localdata[0]

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_power_consumption(data)

    # Part 2
    solution2 = get_oxygen_generator_rating(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

