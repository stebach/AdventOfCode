"""
Solution for day 23 of year 2023
"""

import os
from collections import deque

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    lines = [x.strip() for x in lines]

    start = (lines[0].index('.'),0)
    end = (lines[-1].index('.'), len(lines)-1)
    directions = ((0,1),(0,-1),(1,0),(-1,0))
    to_check = [start]
    crossings = {
    }
    crossings2 = {
    }
    visited = set()
    visited.add(start)

    while len(to_check) > 0:
        paths = [[[to_check.pop()], False, False]]
        while len(paths) > 0:
            path = paths.pop()
            count = 0
            available = []
            for direction in directions:
                next_point = (path[0][-1][0] + direction[0], path[0][-1][1] + direction[1])
                if next_point[0] > -1 and next_point[1] > -1 and next_point[0] < len(lines[0]) and next_point[1] < len(lines):
                    if lines[next_point[1]][next_point[0]] == '.':
                        count += 1
                        if next_point not in visited or (next_point in crossings and next_point != path[0][0]):
                            available.append((next_point, False, False))
                    elif lines[next_point[1]][next_point[0]] in 'v^><':
                        count += 1
                        if next_point not in visited or (next_point in crossings and next_point != path[0][0]):
                            if 'v^><'.index(lines[next_point[1]][next_point[0]]) == directions.index(direction):
                                available.append((next_point, True, False))
                            else:
                                available.append((next_point, False, True))
                    elif lines[next_point[1]][next_point[0]] != '#':
                        print(lines[next_point[1]][next_point[0]])
                        exit()
            if count > 2 or end in [x[0] for x in available]:
                if len(path[0]) == 1:
                    for a in available:
                        paths.append([[path[0][0], a[0]], a[1], a[2]])
                        visited.add(a[0])
                else:
                    if end in [x[0] for x in available]:
                        path[0].append(available[0][0])
                        if available[0][1]:
                            path[1] = True
                        elif available[0][2]:
                            path[2] = True
                    if path[0][0] not in crossings:
                        crossings[path[0][0]] = {}
                        crossings2[path[0][0]] = {}
                    if path[0][-1] not in crossings:
                        crossings[path[0][-1]] = {}
                        crossings2[path[0][-1]] = {}
                    if not path[2]:
                        crossings[path[0][0]][path[0][-1]] = len(path[0]) - 1
                    crossings2[path[0][0]][path[0][-1]] = len(path[0]) - 1
                    if not path[1]:
                        crossings[path[0][-1]][path[0][0]] = len(path[0]) - 1
                    crossings2[path[0][-1]][path[0][0]] = len(path[0]) - 1
                    if path[0][-1] != end:
                        to_check.append(path[0][-1])
            else:
                path[0].append(available[0][0])
                visited.add(available[0][0])
                if available[0][1]:
                    path[1] = True
                elif available[0][2]:
                    path[2] = True
                paths.append(path)

    return (
        start,
        end,
        crossings,
        crossings2
    )

def get_max(current, goal, steps, prev, dict):
    if current == goal:
        return steps
    max = 0
    prev.append(current)
    for next in dict[current]:
        if not next in prev:
            check = get_max(next, goal, steps + dict[current][next], prev, dict)
            if check > max:
                max = check
    prev.pop()
    return max

def part1(data):
    """Solve part 1"""
    prev = deque()
    prev.append(data[0])
    return get_max(data[0],data[1], 0, prev, data[2])

def part2(data):
    """Solve part 2"""
    prev = deque()
    prev.append(data[0])
    return get_max(data[0],data[1], 0, prev, data[3])

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
