"""
Solution for day 11 of year 2024
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return list(map(parse_line, inputdata.readlines()))[0]

def parse_line(line):
    return [int(x) for x in line.strip().split(' ')]

def number_of_stones(data, amount):
    cache = {}
    total = 0
    for stone in data:
        total += get_stone_result(stone, amount, cache)
    return total

def get_stone_result(stone, amount, cache):
    if amount == 0:
        return 1
    if stone not in cache:
        cache[stone] = {}
    if amount in cache[stone]:
        return cache[stone][amount]
    for i in range(1, amount + 1):
        if i not in cache[stone]:
            if stone == 0:
                cache[stone][i] = get_stone_result(1, i - 1, cache)
            elif len(str(stone)) % 2 == 0:
                strval = str(stone)
                cache[stone][i] = get_stone_result(int(strval[:len(strval)//2]), i - 1, cache) \
                     + get_stone_result(int(strval[len(strval)//2:]), i - 1, cache)
            else:
                cache[stone][i] = get_stone_result(stone * 2024, i - 1, cache)
    return cache[stone][amount]

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = number_of_stones(data, 25)

    # Part 2
    solution2 = number_of_stones(data, 75)
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
    #opt = z3.Optimize()
    #x = z3.Int('x')
    #y = z3.Int('y')
    #z = z3.Int('z')
    #count = z3.Int('count')
    #opt.maximize(count)
    #if opt.check() == z3.sat:
    #    model = opt.model()

    print('cache')
    # from functools import lru_cache 

    print('regex')
    # import regex
    # pattern = r'([0-9]|one|two|three|four|five|six|seven|eight|nine)'
    # result = regex.findall(pattern, data, overlapped=True)
    # for match in regex.finditer(r'mul\((\d+),(\d+)\)|do(n\'t)?\(\)', data):
    #    if match.group(0) in ('do()', 'don\'t()'):
