"""
Solution for day 19 of year 2020
"""

import os
import regex
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())


def parse_lines(lines):
    rules = {}
    messages = []
    line = lines.pop(0).strip()
    while len(line) > 0:
        parts = line.split(': ',1)
        if parts[1][0] == '"' and parts[1][-1] == '"':
            rules[int(parts[0])] = parts[1][1:-1]
        else:
            rules[int(parts[0])] = [[int(y) for y in x.split(' ')] for x in parts[1].split(' | ')]
        line = lines.pop(0).strip()
    while len(lines) > 0:
        messages.append(lines.pop(0).strip())

    return (
        rules,
        messages
    )

def create_regex(data, pos = 0):
    if type(data[pos]) == str:
        return data[pos]
    new_data = [''.join([create_regex(data, x) for x in y]) for y in data[pos]]
    if len(new_data) == 1:
        data[pos] = new_data[0]
    else:
        data[pos] = '(' + '|'.join(new_data) + ')'
    return data[pos]

def solve(data):
    """Solve the puzzle for the given input"""
    data_copy = deepcopy(data)
    # Part 1
    pattern = '^' + create_regex(data[0],0) + '$'
    solution1 = sum([regex.match(pattern, x) != None for x in data[1]])

    # Part 2
    create_regex(data_copy[0], 42)
    create_regex(data_copy[0], 31)
    data_copy[0][8] = '(' + data_copy[0][42] + ')+'
    data_copy[0][11] = data_copy[0][42] + '(' + data_copy[0][42] + '(' + data_copy[0][42] + '(' + data_copy[0][42] + '(' + data_copy[0][42] + '(' + data_copy[0][42] + '(' + data_copy[0][42] + data_copy[0][31] + ')?' + data_copy[0][31] + ')?' + data_copy[0][31] + ')?' + data_copy[0][31] + ')?' + data_copy[0][31] + ')?' + data_copy[0][31] + ')?' + data_copy[0][31]
    pattern = '^' + create_regex(data_copy[0],0) + '$'
    solution2 = sum([regex.match(pattern, x) != None for x in data_copy[1]])

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
