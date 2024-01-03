"""
Solution for day 03 of year 2019
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([(x[0], int(x[1:])) for x in line.strip().split(',')])

def get_paths(data):
    directions = {
        'R':(1,0),
        'U':(0,-1),
        'D':(0,1),
        'L':(-1,0),
    }
    paths = [[],[]]
    for idx in range(2):
        pos = (0,0)
        for idx2 in range(len(data[idx])):
            direction = directions[data[idx][idx2][0]]
            for step in range(data[idx][idx2][1]):
                pos = (pos[0] + direction[0], pos[1] + direction[1])
                paths[idx].append(pos)
    return paths

def part1(data):
    """Solve part 1"""
    paths = get_paths(data)
    
    min_distance = 10000000000000000000000
    for point in paths[0]:
        distance = abs(point[0]) + abs(point[1])
        if distance < min_distance:
            if point in paths[1]:
                min_distance = distance
    return min_distance

def part2(data):
    """Solve part 2"""
    paths = get_paths(data)
    min_distance = 10000000000000000000000
    for dist1 in range(len(paths[0])):
        distance = dist1 + 2
        if distance < min_distance:
            if paths[0][dist1] in paths[1]:
                distance += paths[1].index(paths[0][dist1])
                if distance < min_distance:
                    min_distance = distance
    return min_distance

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
