"""
Solution for day 01 of year 2016
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    return tuple([item for x in lines[0].strip().split(', ') for item in [x[0], int(x[1:])]])

def distance(data, get_first_location_visited_twice = False):
    direction = [0,-1]
    pos = [0, 0]
    visited = set([(0,0)])
    for i in range(len(data) // 2):
        if data[i * 2] == 'R':
            direction = [direction[1] * -1, direction[0]]
        else:
            direction = [direction[1], direction[0] * -1]
        newpos = [pos[0] + direction[0] * data[i * 2 + 1], pos[1] + direction[1] * data[i * 2 + 1]]
        if get_first_location_visited_twice:
            x_direction = 1 if pos[0] < newpos[0] else -1
            y_direction = 1 if pos[1] < newpos[1] else -1
            x_start_diff = x_direction
            y_start_diff = y_direction
            if pos[0] == newpos[0]:
                x_start_diff = 0
            if pos[1] == newpos[1]:
                y_start_diff = 0
            for x in range(pos[0] + x_start_diff, newpos[0] + x_direction, x_direction):
                for y in range(pos[1] + y_start_diff, newpos[1] + y_direction, y_direction):
                    if not (x,y) in visited:
                        visited.add((x,y))
                    else:
                        return abs(x) + abs(y)
        pos = newpos
    if get_first_location_visited_twice:
        print(pos)
        print(visited)
        exit()

    return sum([abs(x) for x in pos])

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = distance(data)

    # Part 2
    solution2 = distance(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
