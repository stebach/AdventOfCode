"""
Solution for day 15 of year 2021
"""

import os
import networkx as nx
from math import floor

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return [int(x) for x in [*line.strip()]]

def parse_lines(lines):
    return [x for x in lines]

def find_path(data, inflate_map = False):
    map = []
    multiplier = 1 if not inflate_map else 5
    orig_rows = len(data)
    orig_cols = len(data[0])
    rows = orig_rows * multiplier
    cols = orig_cols * multiplier
    for y in range(rows):
        map.append([])
        for x in range(cols):
            val = data[y % orig_rows][x % orig_cols] + 1 * (floor(y / orig_rows)) + 1 * (floor(x / orig_cols))
            while val > 9:
                val -= 9
            map[y].append(val)

    graph = nx.Graph()
    for y in range(rows):
        for x in range(cols):
            if x > 0:
                graph.add_edge((x-1,y), (x,y), weight={ str(x-1) + "_" + str(y): map[y][x-1], str(x) + "_" + str(y): map[y][x] })
            if y > 0:
                graph.add_edge((x,y-1), (x,y), weight={ str(x) + "_" + str(y-1): map[y-1][x], str(x) + "_" + str(y): map[y][x] })

    path = nx.dijkstra_path(graph, (0,0), (cols-1, rows-1), calc_path_weight)
    risk = 0
    for x in range(1, len(path)):
        risk += map[path[x][1]][path[x][0]]
    return risk

def calc_path_weight(node1, node2, edge):
    return edge['weight']["_".join([str(x) for x in node2])]

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_path(data)

    # Part 2
    solution2 = find_path(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))