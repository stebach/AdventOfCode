"""
Solution for day 06 of year 2020
"""

import os
from functools import reduce

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    data = []
    current_group = []
    lines += ['']
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            data.append(tuple(current_group))
            current_group = []
        else:
            current_group.append(line)
    return tuple(data)

def unique_answers(answers):
    return list(reduce(lambda a,b: set(a).union(set(b)), [[*x] for x in answers]))

def same_answers(answers):
    return list(reduce(lambda a,b: set(a) & set(b), [[*x] for x in answers]))

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum([len(unique_answers(x)) for x in data])

    # Part 2
    solution2 = sum([len(same_answers(x)) for x in data])

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
