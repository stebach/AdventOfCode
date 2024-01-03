"""
Solution for day 06 of year 2019
"""

import os
import networkx as nx
import matplotlib.pyplot as plt

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple(line.strip().split(')'))

def parse_lines(lines):
    return [x for x in lines]

def part1(data):
    """Solve part 1"""
    map = nx.Graph()
    for x in data:
        map.add_edge(x[0],x[1])

    return sum([len(nx.shortest_path(map, 'COM',x)) - 1 for x in  map.nodes])
    

def part2(data):
    """Solve part 2"""
    map = nx.Graph()
    for x in data:
        map.add_edge(x[0],x[1])
    return len(nx.shortest_path(map, 'YOU','SAN')) - 3


def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
