"""
Solution for day 13 of year 2016
"""

import os
import networkx as nx

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return int(inputdata.read())

def find_route(start, goal, number):
    open_spaces = set()
    graph = nx.Graph()
    max_x = goal[0]
    max_y = goal[1]
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if is_open_space((x,y), number):
                add_to_map(graph, (x,y), open_spaces)

    while not nx.has_path(graph, start, goal):
        max_x = max_x + 1
        max_y = max_y + 1
        for x in range(max_x):
            if is_open_space((x,max_y), number):
                add_to_map(graph, (x,max_y), open_spaces)
        for y in range(max_y):
            if is_open_space((max_x, y), number):
                add_to_map(graph, (max_x ,y), open_spaces)
        if is_open_space((max_x, max_y), number):
            add_to_map(graph, (max_x ,max_y), open_spaces)

    return len(nx.shortest_path(graph, start,goal)) - 1

def is_open_space(pos, number):
    return len([x for x in [*bin((pos[0] + 3) * pos[0] + 2 * pos[0] * pos[1] + (pos[1] + 1) * pos[1] + number)[2:]] if x == '1']) % 2 == 0

def flood(start, steps, number):
    reachable = set([start])
    open_space = set()
    wall = set()

    queue = [(0,start)]

    directions = ((0, -1), (0, 1), (1, 0), (-1, 0))

    while len(queue) > 0:
        currentsteps, pos = queue.pop(0)
        for direction in directions:
            pos2 = (pos[0] + direction[0], pos[1] + direction[1])
            if pos2 in wall or pos2 in reachable or pos2[0] < 0 or pos2[1] < 0:
                continue
            if not pos2 in open_space:
                if is_open_space(pos2, number):
                    open_space.add(pos2)
                else:
                    wall.add(pos2)
                    continue
            reachable.add(pos2)
            if currentsteps < steps -1:
                queue.append((currentsteps + 1, pos2))
    return len(reachable)



def add_to_map(graph, pos, others):
    others.add(pos)
    graph.add_node(pos)
    if pos[0] > 0 and (pos[0] - 1, pos[1]) in others:
        graph.add_edge((pos[0] - 1, pos[1]), pos)
    if pos[1] > 0 and (pos[0], pos[1] - 1) in others:
        graph.add_edge((pos[0], pos[1] - 1), pos)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_route((1,1), (31,39), data)

    # Part 2
    solution2 = flood((1,1), 50, data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
