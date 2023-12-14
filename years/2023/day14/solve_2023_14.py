"""
Solution for day 14 of year 2023
"""

import os
from functools import cmp_to_key, lru_cache

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def move_rocks(rocks):
    rocklist = list(rocks)
    for pos in range(len(rocks) - 1):
        if rocklist[len(rocks) - 2 - pos] == 'O':
            rocklist[len(rocks) - 2 - pos] = '.'
            target = len(rocks) - 1
            for pos2 in range(len(rocks) - pos - 1, len(rocks)):
                if rocklist[pos2] in '#O':
                    target = pos2 - 1 
                    break
            rocklist[target] = 'O'
    return tuple(rocklist)

@lru_cache
def tilt(rockmap, spin = False):

    rockmap = [[rockmap[len(rockmap) - 1 - y][x] for y in range(len(rockmap))] for x in range(len(rockmap[0]))]
    rockmap = list(map(move_rocks, rockmap))
    if spin:
        rockmap = [[rockmap[len(rockmap) - 1 - y][x] for y in range(len(rockmap))] for x in range(len(rockmap[0]))]
        rockmap = list(map(move_rocks, rockmap))
        rockmap = [[rockmap[len(rockmap) - 1 - y][x] for y in range(len(rockmap))] for x in range(len(rockmap[0]))]
        rockmap = list(map(move_rocks, rockmap))
        rockmap = [[rockmap[len(rockmap) - 1 - y][x] for y in range(len(rockmap))] for x in range(len(rockmap[0]))]
        rockmap = list(map(move_rocks, rockmap))
    else:
        rockmap = [[rockmap[y][len(rockmap[0]) - x - 1] for y in range(len(rockmap))] for x in range(len(rockmap[0]))]
    return tuple([tuple(x) for x in rockmap])

def part1(data):
    """Solve part 1"""
    tilted = tilt(data)
    return sum([sum([len(tilted) - x for y in tilted[x] if y == 'O']) for x in range(len(tilted))])

def part2(data):
    """Solve part 2"""
    seen = []
    for x in range(1_000_000_000):
        data = tilt(data, True)
        key = "".join(["".join(x) for x in data])
        if key in seen:
            jump = len(seen) - seen.index(key)
            todo = (1_000_000_000 - len(seen) - 1) % jump
            for y in range(todo):
                data = tilt(data, True)
            break
        seen.append(key)
    return sum([sum([len(data) - x for y in data[x] if y == 'O']) for x in range(len(data))])

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
