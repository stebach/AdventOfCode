"""
Solution for day 21 of year 2023
"""

import os
from math import ceil, floor

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    start = None
    rocks = []
    for y in range(len(lines)):
        for x in range(len(lines[y].strip())):
            if lines[y][x] == '#':
                rocks.append((x,y))
            elif lines[y][x] == 'S':
                start = (x,y)
    return (
        start,
        (len(lines[0].strip()),len(lines)),
        tuple(rocks),
    )

def part1(data, steps=64):
    """Solve part 1"""
    possibilites = [data[0]]
    history = []
    visited = set()
    directions = ((0,1),(0,-1),(1,0),(-1,0))

    for step in range(steps):
        new_posibilities = []
        for start in possibilites:
            for direction in directions:
                to_check = (start[0] + direction[0], start[1] + direction[1])
                if to_check[0] > -1 and to_check[1] > -1 and to_check[0] < data[1][0] and to_check[1] < data[1][1] and to_check not in data[2] and to_check not in visited:
                    visited.add(to_check)
                    new_posibilities.append(to_check)
        if step == 0:
            history.append([])
        else:
            history.append(possibilites)
        possibilites = new_posibilities
        while len(history) > 2:
            history[2] += [x for x in history[0] if x not in history[2]]
            del history[0]
    
    result = len(possibilites)
    if len(history) > 1:
        result += len(history[0])

    return result

def part2(data, steps=26501365):
    """Solve part 2"""
    possibilites = [data[0]]
    history1 = set()
    history2 = set()
    visited = set()
    directions = ((0,1),(0,-1),(1,0),(-1,0))

    calc = []

    for step in range(data[1][0]*2+2):
        new_posibilities = []
        for start in possibilites:
            for direction in directions:
                to_check = (start[0] + direction[0], start[1] + direction[1])
                if (to_check[0] % data[1][0], to_check[1] % data[1][1]) not in data[2] and to_check not in visited:
                    visited.add(to_check)
                    new_posibilities.append(to_check)
        if step > 0:
            tmp = history2
            history2 = history1
            history1 = set(possibilites).union(tmp)
        possibilites = new_posibilities

        result = len(possibilites)
        if len(history2) > 1:
            result += len(history2)
        calc.append(result)

    # get the first diff
    first_entry = steps % data[1][0]
    first_diff = calc[first_entry + data[1][0] -1 ] - calc[first_entry - 1]

    # additional steps of [grid with] to take
    additional_steps = int((steps - first_entry) / data[1][0])

    # get diff of diffs
    diff1 = calc[data[1][0]] - calc[0]
    diff2 = calc[data[1][0]*2] - calc[data[1][0]]
    diff_diff = diff2 - diff1

    # calculate
    return calc[first_entry-1] + first_diff * additional_steps + int((additional_steps * (additional_steps - 1))/2) * diff_diff

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
