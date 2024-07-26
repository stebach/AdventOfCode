"""
Solution for day 12 of year 2017
"""

import os
import networkx as nx

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().split(' <-> ')
    return (int(line[0]), tuple(int(x) for x in line[1].split(',')))

def count_connections(data, start):
    graph = nx.Graph()
    for (pos_from, pos_tos) in data:
        for pos_to in pos_tos:
            graph.add_edge(pos_from, pos_to)

    return len(nx.node_connected_component(graph, start))

def count_groups(data):
    graph = nx.Graph()
    for (pos_from, pos_tos) in data:
        for pos_to in pos_tos:
            graph.add_edge(pos_from, pos_to)
    groups = 0
    to_find = [x[0] for x in data]
    while len(to_find):
        to_remove = list(nx.node_connected_component(graph, to_find[0]))
        to_find = [x for x in to_find if x not in to_remove]
        groups += 1
    return groups

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_connections(data, 0)

    # Part 2
    solution2 = count_groups(data)
    print(solution2)
    exit()
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
