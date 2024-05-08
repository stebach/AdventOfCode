"""
Solution for day 11 of year 2015
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read().strip()

def string_to_password(data):
    return [ord(x) for x in data]

def password_to_string(data):
    return "".join([chr(x) for x in data])

def increment_password(data):
    pos = 1
    data[-pos] += 1
    while data[-pos] > 122:
        data[-pos] = 97
        pos += 1
        data[-pos] += 1
    return data

def validate_increasing_straight(data):
    for pos in range(5):
        if data[pos + 1] == data[pos] + 1 and data[pos + 2] == data[pos] + 2:
            return True
    return False

def validate_no_forbidden_letters(data):
    return 105 not in data and 111 not in data and 108 not in data

def validate_two_pairs(data):
    pairs = []
    for x in range(7):
        if data[x] == data[x + 1]:
            pairs.append(x)
    for pair1 in range(0, len(pairs) -1):
        for pair2 in range(pair1, len(pairs)):
            if abs(pairs[pair2] - pairs[pair1]) > 1:
                return True
    return False

def validate_password(data):
    return validate_no_forbidden_letters(data) and validate_increasing_straight(data) and validate_two_pairs(data)

def find_next_valid_password(data):
    next_password = increment_password(data)
    while not validate_password(next_password):
        next_password = increment_password(next_password)
    return next_password

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = password_to_string(find_next_valid_password(string_to_password(data)))

    # Part 2
    solution2 = password_to_string(find_next_valid_password(string_to_password(solution1)))

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
    #graph = nx.DiGraph() #directional graph
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
