"""
Solution for day 20 of year 2018
"""

import os
from collections import deque
import networkx
import matplotlib.pyplot as plt

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read().strip()

def parse_line(line):
    return line.strip()

def parse_lines(lines):
    return [x for x in lines]

directions = ((0,-1), (1,0), (0,1), (-1,0))

def create_map(map, data, pos):
    while len(data) > 0:
        if data[0] in 'NESW':
            direction = directions['NESW'.index(data[0])]
            pos2 = (pos[0] + direction[0], pos[1] + direction[1])
            map.add_edge(pos,pos2)
            pos = pos2
            data.popleft()
        elif data[0] == '(':
            data.popleft()
            create_map(map, data, pos)
            while data[0] == '|':
                data.popleft()
                create_map(map, data, pos)
            data.popleft()
        elif data[0] in '|)':
            return
        elif data[0] in '^$':
            data.popleft()
        else:
            print("unknown: " + data[0])
            exit()
    return

def part1(data):
    """Solve part 1"""
    data = deque([*data])
    map = networkx.Graph()
    create_map(map, data, (0,0))
    max_distance = 0
    for node in map.nodes:
        distance = len(networkx.shortest_path(map, (0,0), node))
        if distance > max_distance:
            max_distance = distance
    return max_distance - 1

def part2(data):
    """Solve part 2"""
    data = deque([*data])
    map = networkx.Graph()
    create_map(map, data, (0,0))
    count = 0
    for node in map.nodes:
        distance = len(networkx.shortest_path(map, (0,0), node))
        if distance > 1000:
            count += 1
    return count

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
