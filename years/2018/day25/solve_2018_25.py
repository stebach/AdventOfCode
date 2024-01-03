"""
Solution for day 25 of year 2018
"""

import os
import networkx as nx
import matplotlib.pyplot as plt

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([int(x) for x in line.strip().split(',')])

def part1(data):
    """Solve part 1"""
    map = nx.Graph()
    for x in range(len(data)-1):
        map.add_node(data[x])
        for y in range(x+1, len(data)):
            distance = 0
            if sum([abs(data[x][z] - data[y][z]) for z in range(4)]) <= 3:
                map.add_edge(data[x], data[y])
    map.add_node(data[len(data)-1])
    return (sum(1 for x in nx.connected_components(map)))


def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    return (solution1,)

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
