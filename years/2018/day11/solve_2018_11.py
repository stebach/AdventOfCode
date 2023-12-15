"""
Solution for day 11 of year 2018
"""

import os
from math import floor

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return int(inputdata.read())

def parse_line(line):
    return line.strip()

def parse_lines(lines):
    return [x for x in lines]

def power_level(x, y, serial_number):
    return (floor(((x+10) * y + serial_number) * (x+10) / 100) % 10) - 5


def get_max_power(serial_number, size = 3):
    grid = [[power_level(x,y, serial_number) for x in range(300)] for y in range(300)]
    for y in range(300):
        for x in range(300):
            grid[y][x] = grid[y][x] + (grid[y-1][x] if y > 0 else 0) + (grid[y][x-1] if x > 0 else 0) - (grid[y-1][x-1] if x > 0 and y > 0 else 0)

    if size == 300:
        return (0,0,0)

    grid2 = [[grid[y][x] - grid[y-size][x] - grid[y][x-size] + grid[y-size][x-size] for x in range(size,300)] for y in range(size, 300)]

    max_power =max([max(x) for x in grid2])

    y = grid2.index([x for x in grid2 if max_power in x][0])
    x = grid2[y].index(max_power)

    return (x+1,y+1,max_power)

def part1(data):
    """Solve part 1"""
    result = get_max_power(data)
    
    return (result[0], result[1])

def part2(data):
    """Solve part 2"""
    result = [get_max_power(data,x + 1) for x in range(0,300)]
    max_power = max([x[2] for x in result])
    pos = result.index([x for x in result if x[2] == max_power][0])
    return (result[pos][0],result[pos][1],pos+1)

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
