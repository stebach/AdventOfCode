"""
Solution for day 06 of year 2023
"""

import os
import math

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(tuple(map(lambda line: line.strip(), inputdata.readlines())))

def parse_lines(lines):
    times = [int(x) for x in lines[0].split(" ")[1:] if x != '']
    distances = [int(x) for x in lines[1].split(" ")[1:] if x != '']

    return [[times[x], distances[x]] for x in range(len(times))]

def travel_distance(button_time, total_time):
    return (total_time - button_time) * button_time

def part1(data):
    """Solve part 1"""
    return math.prod([len([x for x in [(data[y][0] - x) * x for x in range(data[y][0])] if x > data[y][1]]) for y in range(len(data))])

def find_first(time, distance, start, step):
    button = start
    while abs(step) >= 1:
        while (time - button) * button <= distance:
            button = button + step
        if button - step >= 0 and button - step <= time:
            button = button - step
        step = int(step / 10)
    return button
            

def part2(data):
    """Solve part 2"""
    time = int("".join([str(x[0]) for x in data]))
    distance = int("".join([str(x[1]) for x in data]))
    first = find_first(time, distance, 0, 1000) + 1
    last = find_first(time, distance, time, -1000) - 1

    return last - first + 1

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
