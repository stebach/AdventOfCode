"""
Solution for day 12 of year 2020
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()
    return (line[0],int(line[1:]))

def get_manhattan_distance(data):
    pos = [0,0]
    direction = [1,0]
    for x in data:
        if x[0] == 'F':
            pos[0] += x[1] * direction[0]
            pos[1] += x[1] * direction[1]
        elif x[0] == 'N':
            pos[1] -= x[1]
        elif x[0] == 'S':
            pos[1] += x[1]
        elif x[0] == 'E':
            pos[0] += x[1]
        elif x[0] == 'W':
            pos[0] -= x[1]
        elif x[0] == 'R':
            for y in range(int(x[1] / 90)):
                direction = [direction[1]*-1, direction[0]]
        elif x[0] == 'L':
            for y in range(int(x[1] / 90)):
                direction = [direction[1], direction[0]*-1]
        else:
            print(x)
            exit()
    return abs(pos[0]) + abs(pos[1])

def waypoint_movement(data):
    pos = [0,0]
    waypoint = [10,-1]
    for x in data:
        if x[0] == 'F':
            pos[0] += x[1] * waypoint[0]
            pos[1] += x[1] * waypoint[1]
        elif x[0] == 'N':
            waypoint[1] -= x[1]
        elif x[0] == 'S':
            waypoint[1] += x[1]
        elif x[0] == 'E':
            waypoint[0] += x[1]
        elif x[0] == 'W':
            waypoint[0] -= x[1]
        elif x[0] == 'R':
            for y in range(int(x[1] / 90)):
                waypoint = [waypoint[1]*-1, waypoint[0]]
        elif x[0] == 'L':
            for y in range(int(x[1] / 90)):
                waypoint = [waypoint[1], waypoint[0]*-1]
        else:
            print(x)
            exit()
    return abs(pos[0]) + abs(pos[1])

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_manhattan_distance(data)
    # Part 2
    solution2 = waypoint_movement(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
