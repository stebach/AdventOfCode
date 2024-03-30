"""
Solution for day 14 of year 2021
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = [{},{},{}]
    polymer = lines.pop(0).strip()
    for x in range(len(polymer)-1):
        combination = polymer[x:x+2]
        if combination not in result[0]:
            result[0][combination] = 0
        result[0][combination] += 1
        if x == 0:
            result[1][polymer[x]] = 1
        part = polymer[x + 1]
        if not part in result[1]:
            result[1][part] = 0
        result[1][part] += 1

    lines.pop(0)
    for line in lines:
        line = line.strip().split(' -> ')
        result[2][line[0]] = line[1]
    return result

def steps(data, steps_to_take):
    local_data = deepcopy(data)
    for step_to_take in range(steps_to_take):
        new_combinations = {}
        for x in local_data[0]:
            add_to_dict(new_combinations, x[0] + local_data[2][x], local_data[0][x])
            add_to_dict(new_combinations, local_data[2][x] + x[1], local_data[0][x])
            add_to_dict(local_data[1], local_data[2][x], local_data[0][x])
        local_data[0] = new_combinations
    return local_data

def add_to_dict(the_dict, key, val):
    if key not in the_dict:
        the_dict[key] = 0
    the_dict[key] += val

def calc_result(data, steps_to_take):
    local_data = steps(data, steps_to_take)
    numbers = [local_data[1][x] for x in local_data[1]]
    return max(numbers) - min(numbers)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = calc_result(data, 10)

    # Part 2
    solution2 = calc_result(data, 40)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

