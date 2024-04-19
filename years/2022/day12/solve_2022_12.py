"""
Solution for day 12 of year 2022
"""

import os
import networkx as nx

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = []
    start = None
    goal = None
    grid = [[ord(y) - 97 for y in [*x.strip()]] for x in lines]
    for (y, line) in enumerate(grid):
        for x, ordnum in enumerate(line):
            if ordnum == -14:
                start = (x,y)
                grid[y][x] = 0
            elif ordnum == -28:
                goal = (x,y)
                grid[y][x] = 25
    return tuple([grid, start, goal])

def steps(data, find_shortest = False):
    graph = nx.DiGraph()
    possible_starts = []
    for (y, line) in enumerate(data[0]):
        for (x, point) in enumerate(line):
            if point == 0:
                possible_starts.append((x,y))
            if x > 0 and data[0][y][x-1] <= point + 1:
                graph.add_edge((x,y), (x-1,y))
            if x < len(line) - 1 and data[0][y][x+1] <= point + 1:
                graph.add_edge((x,y), (x+1,y))
            if y > 0 and data[0][y-1][x] <= point + 1:
                graph.add_edge((x,y), (x,y-1))
            if y < len(data[0]) - 1 and data[0][y+1][x] <= point + 1:
                graph.add_edge((x,y), (x,y+1))
    if not find_shortest:
        return len(nx.dijkstra_path(graph, data[1], data[2])) - 1
    waylengths = []
    for start in possible_starts:
        if nx.has_path(graph, start, data[2]):
            waylengths.append(len(nx.dijkstra_path(graph, start, data[2])) - 1)
    return min(waylengths)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = steps(data)

    # Part 2
    solution2 = steps(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

