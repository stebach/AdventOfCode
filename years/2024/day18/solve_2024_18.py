"""
Solution for day 18 of year 2024
"""

import os
import networkx as nx

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([int(x) for x in line.strip().split(',')])

def shortest_path(data, size, bytes):
    graph = nx.Graph()
    for y in range(size + 1):
        for x in range(size + 1):
            if x < size and (x, y) not in data[:bytes] and (x + 1, y) not in data[:bytes]:
                graph.add_edge((x, y), (x + 1, y))
            if y < size and (x, y) not in data[:bytes] and (x, y + 1) not in data[:bytes]:
                graph.add_edge((x, y), (x, y + 1))
    
    return nx.shortest_path_length(graph, (0, 0), (size, size))

def find_blocking(data, size):
    graph = nx.Graph()
    for y in range(size + 1):
        for x in range(size + 1):
            if x < size:
                graph.add_edge((x, y), (x + 1, y))
            if y < size:
                graph.add_edge((x, y), (x, y + 1))

    for x, y in data:
        graph.remove_node((x, y))
        if not nx.has_path(graph, (0, 0), (size, size)):
            return (x, y)

def solve(data ,size=70, bytes=1024):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = shortest_path(data, size, bytes)

    # Part 2
    solution2 = ",".join([str(x) for x in find_blocking(data, size)])

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
