"""
Solution for day 25 of year 2023
"""

import os
import networkx
import matplotlib.pyplot as plt

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {}
    for line in lines:
        line = line.strip().split(': ')
        for x in line[1].split(' '):
            if not x in result:
                result[x] = {}
            if not line[0] in result:
                result[line[0]] = {}
            result[line[0]][x] = 0
            result[x][line[0]] = 0

    return result

def part1(data):
    """Solve part 1"""
    graph = networkx.Graph()
    for x in data:
        for y in data[x]:
            graph.add_edge(x,y)

    nodes = [x for x in set(data)]
    for x in range(1,len(nodes)):
        cuts = networkx.minimum_edge_cut(graph, nodes[0], nodes[x])
        if len(cuts) == 3:
            for cut in cuts:
                graph.remove_edge(cut[0], cut[1])
            group1 = networkx.node_connected_component(graph, nodes[0])
            group2 = networkx.node_connected_component(graph, nodes[x])
            return len(group1) * len(group2)
    return 0

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    return solution1, None

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
