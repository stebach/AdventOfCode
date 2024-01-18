"""
Solution for day 20 of year 2019
"""

import os
import networkx as nx
import matplotlib.pyplot as plt

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip("\n"), inputdata.readlines()))

def init_graph(data):
    positions = {}
    named_positions = []
    thickness = 0
    for x in range(2,100000):
        if data[x][x] == ' ':
            thickness = x-2
            break

    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if ord(col) >= 65 and ord(col) <= 90:
                if y == 0:
                    positions[(y+2,x)] = (col + data[y+1][x], 0)
                    named_positions.append((y+2,x))
                elif x == 0:
                    positions[(y,x+2)] = (col + data[y][x+1], 0)
                    named_positions.append((y,x+2))

                elif y == thickness + 2:
                    positions[(y-1,x)] = (col + data[y+1][x], 1)
                    named_positions.append((y-1,x))
                elif x == thickness + 2:
                    positions[(y,x-1)] = (col + data[y][x+1], 1)
                    named_positions.append((y,x-1))

                elif y == len(data) - 4 - thickness and data[y+1][x] != ' ':
                    positions[(y+2,x)] = (col + data[y+1][x], 1)
                    named_positions.append((y+2,x))
                elif x == len(row) - thickness - 4 and data[y][x+1] != ' ':
                    positions[(y,x+2)] = (col + data[y][x+1], 1)
                    named_positions.append((y,x+2))

                elif y == len(data) - 2:
                    positions[(y-1,x)] = (col + data[y+1][x], 0)
                    named_positions.append((y-1,x))
                elif x == len(row) - 2:
                    positions[(y,x-1)] = (col + data[y][x+1], 0)
                    named_positions.append((y,x-1))

                elif y != 1 and x != 1 and y != thickness + 3 and x != thickness + 3 and y != len(data) - thickness - 3  and x != len(row) - thickness - 3 and  y != len(data) - 1 and x != len(row) - 1:
                    print("Error")
                    exit()

            elif col == '.':
                if (y,x) not in positions and (y,x) not in positions:
                    positions[(y,x)] = ('.',-1)

    graph1 = nx.Graph()

    items = list(positions.items())
    for i in range(len(items) - 1):
        for i2 in range(i + 1, len(items)):
            distance = abs(items[i][0][0] - items[i2][0][0]) + abs(items[i][0][1] - items[i2][0][1])
            if distance == 1:
                graph1.add_edge(items[i][0],items[i2][0])

    return (graph1, positions, named_positions)

def solve_single(data):
    graph1, positions, named_positions = init_graph(data)

    graph2 = nx.Graph()
    for i in range(len(named_positions) -1):
        for i2 in range(i + 1, len(named_positions)):
            if not nx.has_path(graph1, named_positions[i], named_positions[i2]):
                continue
            path = nx.shortest_path_length(graph1, named_positions[i], named_positions[i2])
            nx.add_path(graph2, (positions[named_positions[i]][0],positions[named_positions[i2]][0]), weight=path+1)

    path = nx.shortest_path_length(graph2, 'AA', 'ZZ', 'weight')

    return path-1

def solve_nested(data):
    graph1, positions, named_positions = init_graph(data)

    max_levels = 30
    graph2 = nx.Graph()
    for i in range(len(named_positions) -1):
        name1 = positions[named_positions[i]]
        for i2 in range(i + 1, len(named_positions)):
            name2 = positions[named_positions[i2]]
            if not nx.has_path(graph1, named_positions[i], named_positions[i2]):
                continue
            path = nx.shortest_path_length(graph1, named_positions[i], named_positions[i2])

            for level in range(max_levels):
                if (name1[0] in ('AA','ZZ') or name2[0] in ('AA','ZZ')) and level > 0:
                    continue
                nx.add_path(graph2, (name1[0] + "_" + str(name1[1]) + "_" + str(level),name2[0] + "_" + str(name2[1]) + "_" + str(level)), weight=path+1)

    for level in range(max_levels):
        for i in range(len(named_positions)):
            name1 = positions[named_positions[i]]
            if name1[0] in ('AA','ZZ'):
                continue
            nx.add_path(graph2, (name1[0] + "_1_" + str(level),name1[0] + "_0_" + str(level + 1)), weight=0)

    path = nx.shortest_path_length(graph2, 'AA_0_0', 'ZZ_0_0', 'weight')

    return path-1

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = solve_single(data)

    # Part 2
    solution2 = solve_nested(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
