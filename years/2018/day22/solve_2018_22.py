"""
Solution for day 22 of year 2018
"""

import os
import numpy as np
from queue import PriorityQueue

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    return tuple([int(lines[0].strip()[7:])] + [int(x) for x in lines[1].strip()[8:].split(',')])

def part1(data):
    """Solve part 1"""
    depth, target_x, target_y = data
    grid = np.zeros([target_y + 1, target_x + 1],int)

    for row in range(target_y + 1):
        for col in range(target_x + 1):
            geologic_index = 0
            if (col,row) not in ((0,0),(target_x, target_y)):
                if row == 0:
                    geologic_index = col * 16807
                elif col == 0:
                    geologic_index = row * 48271
                else:
                    geologic_index = grid[row-1][col] * grid[row][col-1]
            grid[row][col] = (geologic_index + depth) % 20183

    return sum([sum([x%3 for x in y]) for y in grid])

def part2(data):
    """Solve part 2"""
    depth, target_x, target_y = data
    expand = 1000
    grid = np.zeros([target_y + expand + 1, target_x + expand + 1],int)

    for row in range(target_y + expand + 1):
        for col in range(target_x + expand + 1):
            geologic_index = 0
            if (col,row) not in ((0,0),(target_x, target_y)):
                if row == 0:
                    geologic_index = col * 16807
                elif col == 0:
                    geologic_index = row * 48271
                else:
                    geologic_index = grid[row-1][col] * grid[row][col-1]
            grid[row][col] = (geologic_index + depth) % 20183

    grid = [[x % 3 for x in y] for y in grid]

    # 0 = rocky
    # 1 = wet
    # 2 = narrow

    # 0 = nothing
    # 1 = torch
    # 2 = climing gear

    todo = PriorityQueue()
    todo.put((0, (0,0), 1))
    visited = set()
    directions = ((0,1),(0,-1),(1,0),(-1,0))
    valid_tools = {
        (0,1): 2,
        (1,0): 2,
        (0,2): 1,
        (2,0): 1,
        (1,2): 0,
        (2,1): 0
    }
    while True:
        if todo.qsize() == 0:
            print("err: todo empty")
            exit()
        check = todo.get()
        if check[1] == (target_x,target_y):
            if check[2] == 1:
                return check[0]
            else:
                todo.put((check[0] + 7, check[1], 1))
                continue

        for direction in directions:
            next_pos = (check[1][0] + direction[0], check[1][1] + direction[1])
            if next_pos[0] < 0 or next_pos[1] < 0:
                continue
            tool = check[2]
            time = 1
            if grid[next_pos[1]][next_pos[0]] == tool:
                time += 7
                tool = valid_tools[(grid[next_pos[1]][next_pos[0]], grid[check[1][1]][check[1][0]])]
            if (next_pos[0], next_pos[1], tool, time) not in visited:
                visited.add((next_pos[0], next_pos[1], tool, time))
                todo.put((check[0] + time, (next_pos[0], next_pos[1]), tool))


def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
