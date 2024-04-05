"""
Solution for day 20 of year 2021
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = []
    line = lines.pop(0).strip()
    key = {'#':1, '.': 0}
    result.append([key[x] for x in line])
    lines.pop(0)
    result.append([])
    for (y, line) in enumerate(lines):
        for (x, char) in enumerate(line.strip()):
            if char == '#':
                result[1].append([y,x])
    return result

def enhance_twice(data, amount):
    localdata = data
    for i in range(amount):
        newdata = [localdata[0],[]]
        x_vals = [x[1] for x in localdata[1]]
        y_vals = [x[0] for x in localdata[1]]
        tmp = {}
        for y in range(min(y_vals)-2, max(y_vals) + 3):
            for x in range(min(x_vals)-2, max(x_vals) + 3):
                if get_enhance_for_pos(x,y,localdata, tmp) == 1:
                    newdata[1].append([y,x])
        localdata = newdata
    return localdata

def get_enhance_for_pos(x,y,data,tmp):
    for yy in range(y-1, y+2):
        for xx in range(x-1, x+2):
            key = str(yy) + "_" + str(xx)
            if not key in tmp:
                tmpval = (1 if [yy - 1, xx - 1] in data[1] else 0) * 256
                tmpval += (1 if [yy - 1,xx] in data[1] else 0) * 128
                tmpval += (1 if [yy - 1,xx + 1] in data[1] else 0) * 64

                tmpval += (1 if [yy,xx - 1] in data[1] else 0) * 32
                tmpval += (1 if [yy,xx] in data[1] else 0) * 16
                tmpval += (1 if [yy,xx + 1] in data[1] else 0) * 8

                tmpval += (1 if [yy + 1,xx - 1] in data[1] else 0) * 4
                tmpval += (1 if [yy + 1,xx] in data[1] else 0) * 2
                tmpval += (1 if [yy + 1,xx + 1] in data[1] else 0) * 1

                tmp[key] = data[0][tmpval]
    
    pos = tmp[str(y-1) + "_" + str(x-1)] * 256
    pos += tmp[str(y-1) + "_" + str(x)] * 128
    pos += tmp[str(y-1) + "_" + str(x+1)] * 64

    pos += tmp[str(y) + "_" + str(x-1)] * 32
    pos += tmp[str(y) + "_" + str(x)] * 16
    pos += tmp[str(y) + "_" + str(x+1)] * 8

    pos += tmp[str(y+1) + "_" + str(x-1)] * 4
    pos += tmp[str(y+1) + "_" + str(x)] * 2
    pos += tmp[str(y+1) + "_" + str(x+1)] * 1

    return data[0][pos]

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = len(enhance_twice(data, 1)[1])

    # Part 2
    solution2 = len(enhance_twice(data, 25)[1])

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

def tools():
    print('map example:')
    #import networkx as nx
    #import matplotlib.pyplot as plt
    #graph = nx.Graph()
    #graph.add_edge((0,0),(0,1))
    #graph.add_edge((0,1),(1,1))
    #graph.add_edge((1,0),(1,1))
    #nx.shortest_path(graph, (0,0), (1,0))
    #nx.draw(graph, pos={x:x for x in graph.nodes}, with_labels=True)
    #graph.add_edge(1, 2, weight=3)
    #graph.add_edge(1, 3, weight=7, capacity=15, length=342.7)
    #nx.dijkstra_path(graph, (0,0), (1,0))
    #nx.dijkstra_path(graph, (0,0), (1, 0), calc_path_weight)
    #def calc_path_weight(from_node, to_node, edge_attributes):
    #   return xxx
    #plt.show()

    print('numpy:')
    #import numpy as np
    #np.lcm(1,2)
    #np.lcm.reduce([1,2,3,4])

    print('z3:')
    #import z3
    #opt = z3.Solver()
    #a = z3.Int('a')
    #b = z3.Int('b')
    #c = z3.Int('c')
    #opt.add(a < 6, a > 0, b < 6, b > 0, c < 6, c > 0)
    #if opt.check() == z3.unsat:
    #    model = opt.model()
    #    print(model)
    #    print(model[a])
    #    print(model[b])
    #    print(model[c])
