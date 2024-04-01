"""
Solution for day 17 of year 2021
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    return tuple([int(x) for x in "..".join(lines[0].strip()[15:].split(', y=')).split('..')])

def find_highest_y(data):
    result = 0
    for start_yy in range(abs(min(data[2:4])) - 1, 1, -1):
        yy = start_yy
        is_valid = False
        y = 0
        max_y = 0
        while y > min(data[2:4]):
            y += yy
            yy -= 1
            max_y = max(y, max_y)
            if y >= min(data[2:4]) and y <= max(data[2:4]):
                is_valid = True
        if is_valid:
            result = max(max_y, result)
    return result

def find_initial_velocity_count(data):
    valid_y = {}
    valid_x = {}

    for y in range(abs(min(data[2:4])) - 1, min(data[2:4]) -1, -1):
        curr_y = 0
        curr_velocity = y
        steps = 0
        while curr_y >= min(data[2:4]):
            curr_y += curr_velocity
            curr_velocity -= 1
            steps += 1
            if curr_y <= max(data[2:4]) and curr_y >= min(data[2:4]):
                if steps not in valid_y:
                    valid_y[steps] = []
                valid_y[steps].append(y)
    
    max_y_steps = max([x for x in valid_y])

    for x in range(1, max(data[:2]) + 1):
        curr_x = 0
        curr_velocity = x
        steps = 0

        while curr_x <= max(data[:2]) and steps <= max_y_steps:
            curr_x += curr_velocity
            if curr_velocity > 0:
                curr_velocity -= 1
            steps += 1
            if curr_x >= min(data[:2]) and curr_x <= max(data[:2]):
                if steps not in valid_x:
                    valid_x[steps] = []
                valid_x[steps].append(x)
    result = []
    for y in valid_y:
        if y in valid_x:
            for xx in valid_x[y]:
                for yy in valid_y[y]:
                    result.append(str(xx)+","+str(yy))
    return len(set(result))

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_highest_y(data)

    # Part 2
    solution2 = find_initial_velocity_count(data)

    return solution1, solution2

