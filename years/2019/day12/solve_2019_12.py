"""
Solution for day 12 of year 2019
"""

import os
from copy import deepcopy
import numpy as np

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return [int(x.split('=')[1]) for x in line.strip()[1:-1].split(', ')] + [0,0,0]

def move(data):
    # update movement
    for x in range(len(data) -1):
        for y in range(x + 1, len(data)):
            for dimension in range(3):
                diff = (data[x][dimension] < data[y][dimension]) - (data[x][dimension] > data[y][dimension])
                data[x][dimension + 3] += diff
                data[y][dimension + 3] -= diff
    # move
    for x in data:
        for dimension in range(3):
            x[dimension] += x[dimension + 3]

def calc_energy(data):
    return sum([sum([abs(y) for y in x[0:3]]) * sum([abs(y) for y in x[3:6]]) for x in data])

def find_repetition(data):
    dimensions = [
        [[x[0],0,0] + x[3:6] for x in data],
        [[0,x[1],0] + x[3:6] for x in data],
        [[0,0,x[2]] + x[3:6] for x in data]
    ]
    repetitions = []
    for pos, dimension_data in enumerate(dimensions):
        seen = set()
        state = "/".join(["|".join([str(y) for y in x]) for x in dimension_data])
        while state not in seen:
            seen.add(state)
            move(dimension_data)
            state = "/".join(["|".join([str(y) for y in x]) for x in dimension_data])
        repetitions.append(len(seen))
    return np.lcm.reduce(repetitions)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    data2 = deepcopy(data)
    for x in range(1000):
        move(data)
    solution1 = calc_energy(data)
    # Part 2
    solution2 = find_repetition(data2)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
