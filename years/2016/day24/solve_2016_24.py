"""
Solution for day 24 of year 2016
"""

import os
import itertools
import networkx as nx

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())


def parse_lines(lines):
    path = []
    numbers = {}
    for y in enumerate(lines):
        for x in enumerate(y[1].strip()):
            if x[1] != '#':
                path.append((x[0], y[0]))
                if x[1] != '.':
                    numbers[int(x[1])] = (x[0], y[0])
    return (numbers, tuple(path))

def collect_all(data, return_robot = False):
    paths = {}
    keys = list(sorted(data[0]))[1:]

    combinations = list(itertools.permutations(keys, len(keys)))

    graph = nx.Graph()
    directions = ((0,1),(1,0))
    for pos in data[1]:
        for direction in directions:
            check = (pos[0] + direction[0], pos[1] + direction[1])
            if check in data[1]:
                graph.add_edge(pos, check)

    min_distance = 5_000_000_000_000
    winning_comb = None
    while len(combinations) > 0:
        combination = combinations.pop(0)
        idx = 0
        distance = 0
        for nextidx in combination:
            key = str(min([idx, nextidx])) + "_" + str(max([idx, nextidx]))
            if key not in paths:
                paths[key] = nx.shortest_path_length(graph, data[0][idx], data[0][nextidx])
            distance += paths[key]

            if distance >= min_distance:
                break
            idx = nextidx
        if (return_robot):
            key = '0_' + str(idx)
            if key not in paths:
                paths[key] = nx.shortest_path_length(graph, data[0][idx], data[0][0])
            distance += paths[key]

        if distance < min_distance:
            min_distance = distance
            winning_comb = combination

    return min_distance

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = collect_all(data)

    # Part 2
    solution2 = collect_all(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
