"""
Solution for day 11 of year 2023
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(list(map(lambda line: line.strip(), inputdata.readlines())))

def parse_lines(lines):
    galaxies = []
    for nr,line in enumerate(lines):
        galaxies = galaxies + [[nr, x.start()] for x in regex.finditer('#', line)]
    
    return galaxies

def expand(galaxies, factor):
    width = max([x[1] for x in galaxies])
    height = max([x[0] for x in galaxies])

    for row in range(height):
        if len([x for x in galaxies if x[0] == height - 1 - row]) == 0:
            galaxies = list(map(lambda x: [x[0] + (factor - 1 if x[0] > height - 1 - row else 0), x[1]], galaxies))

    for col in range(width):
        if len([x for x in galaxies if x[1] == width -1 - col]) == 0:
            galaxies = list(map(lambda x: [x[0], x[1] + (factor - 1 if x[1] > width - 1 - col else 0)], galaxies))

    return galaxies

def distance(galaxies):
    total = 0
    for x in range(len(galaxies) - 1):
        for y in range(x+1, len(galaxies)):
            total = total + abs(galaxies[x][0] - galaxies[y][0]) + abs(galaxies[x][1] - galaxies[y][1])
    return total

def part1(data):
    """Solve part 1"""
    return  distance(expand(data, 2))

def part2(data, to_expand = 1_000_000):
    """Solve part 2"""
    return  distance(expand(data, to_expand))

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
