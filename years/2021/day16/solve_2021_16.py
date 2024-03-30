"""
Solution for day 16 of year 2021
"""

import os
from copy import deepcopy
import numpy as np

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    return [int(x) for x in [*"".join([bin(int(x,16))[2:].rjust(4,'0') for x in [*lines[0]]])]]

def parse_code(data):
    version = int("".join([str(x) for x in data[:3]]),2)
    type = int("".join([str(x) for x in data[3:6]]),2)
    sub = []
    value = None

    del data[:6]
    if type == 4:
        lastbyte = 1
        binval = ""
        while lastbyte != 0:
            lastbyte = data[0]
            binval += "".join([str(x) for x in data[1:5]])
            del data[:5]
        value = int(binval, 2)
    else:
        lengthtype = data.pop(0)
        if lengthtype == 0:
            sublength = int("".join([str(x) for x in data[0:15]]), 2)
            del data[:15]
            targetlen = len(data) - sublength
            while len(data) != targetlen:
                sub.append(parse_code(data))
        else:
            subcount = int("".join([str(x) for x in data[0:11]]), 2)
            del data[:11]
            while len(sub) < subcount:
                sub.append(parse_code(data))

    return {
        'version': version,
        'type': type,
        'sub': sub,
        'value': value,
    }

def sumup_version_numbers(data):
    return data['version'] + sum([sumup_version_numbers(x) for x in data['sub']])

def calc_value(data):
    if data['type'] == 4:
        return data['value']
    data['sub'] = [calc_value(x) for x in data['sub']]
    if data['type'] == 0: #sum
        return sum(data['sub'])
    if data['type'] == 1: #product
        return np.prod(data['sub'])
    if data['type'] == 2: #min
        return min(data['sub'])
    if data['type'] == 3: #max
        return max(data['sub'])
    if data['type'] == 5: #gt
        if data['sub'][0] > data['sub'][1]:
            return 1
        return 0
    if data['type'] == 6: #lt
        if data['sub'][0] < data['sub'][1]:
            return 1
        return 0
    if data['type'] == 7: #eq
        if data['sub'][0] == data['sub'][1]:
            return 1
        return 0
    print("unknown type: " + str(data['type']))
    exit()

def solve(data):
    """Solve the puzzle for the given input"""
    packets = parse_code(data)
    packets1 = deepcopy(packets)

    # Part 1
    solution1 = sumup_version_numbers(packets1)

    # Part 2
    solution2 = calc_value(packets)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
