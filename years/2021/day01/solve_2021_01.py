"""
Solution for day 01 of year 2021
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: int(line.strip()), inputdata.readlines()))

def get_increases(data, window = 1):
    localdata = [sum(data[x[0]:x[0]+window]) for x in enumerate(data) if x[0] < len(data) + 1 - window]
    return sum([1 if x[1] > localdata[x[0]-1] else 0 for x in enumerate(localdata) if x[0] > 0])


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_increases(data)

    # Part 2
    solution2 = get_increases(data, 3)

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
