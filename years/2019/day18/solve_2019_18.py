"""
Solution for day 18 of year 2019
"""

import os
import networkx as nx
from queue import PriorityQueue
from copy import copy, deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return list(map(lambda line: line.strip(), inputdata.readlines()))


def find_shortest(mapdata):
    keys = {}
    locks = {}
    pos = None
    directions = ((0,1),(1,0),(0,-1),(-1,0))
    graph = nx.Graph()
    for y, row in enumerate(mapdata):
        for x, col in enumerate(row):
            is_path = False
            if ord(col) >= 65 and ord(col) <= 90:
                is_path = True
                locks[(x,y)] = col
            elif ord(col) >= 97 and ord(col) <= 122:
                is_path = True
                keys[col] = (x,y)
            elif col == '.':
                is_path = True
            elif col == '@':
                is_path = True
                pos = (x,y)
            if is_path:
                for direction in directions:
                    check = (direction[0] + x, direction[1] + y)
                    if check[0] >= 0 and check[1] >= 0 and check[1] < len(mapdata) and check[0] < len(mapdata[0]) and mapdata[check[1]][check[0]] in '.@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        graph.add_edge((x,y),check)
                        
    queue = PriorityQueue()
    queue.put([0, [], pos, ()])

    seen = set()
    ways = {}

    while queue.qsize() > 0:
        item = queue.get()
        if len(item[1]) == len(keys):
            return item[0]
        if item[3] in seen:
            continue
        seen.add(item[3])
        for key, keyloc in keys.items():
            if key not in item[1]:
                way = None
                if (item[2], keyloc) in ways:
                    way = ways[(item[2], keyloc)]
                else:
                    way = nx.shortest_path(graph, item[2], keyloc)
                    ways[(item[2], keyloc)] = way
                    ways[(keyloc, item[2])] = [way[-x-1] for x in range(len(way))]
                has_needed_keys = True
                for lock in locks:
                    if lock in way and chr(ord(locks[lock])+32) not in item[1]:
                        has_needed_keys = False
                        break
                if has_needed_keys:
                    new_keys = copy(item[1])
                    new_keys.append(key)
                    check = tuple(sorted(copy(new_keys)) + [way[-1]])
                    if check not in seen:
                        queue.put([item[0] + len(way) - 1, copy(new_keys), way[-1], check])

def find_shortest2(mapdata):
    for y, row in enumerate(mapdata):
        if '.@.' in row:
            idx = row.index('.@.')
            mapdata[y-1] = mapdata[y-1][0:idx] + '@#@' + mapdata[y-1][idx+3:]
            mapdata[y] = mapdata[y][0:idx] + '###' + mapdata[y][idx+3:]
            mapdata[y+1] = mapdata[y+1][0:idx] + '@#@' + mapdata[y+1][idx+3:]
    keys = {}
    locks = {}
    pos = []
    directions = ((0,1),(1,0),(0,-1),(-1,0))
    graph = nx.Graph()
    for y, row in enumerate(mapdata):
        for x, col in enumerate(row):
            is_path = False
            if ord(col) >= 65 and ord(col) <= 90:
                is_path = True
                locks[(x,y)] = col
            elif ord(col) >= 97 and ord(col) <= 122:
                is_path = True
                keys[col] = (x,y)
            elif col == '.':
                is_path = True
            elif col == '@':
                is_path = True
                pos.append((x,y))
            if is_path:
                for direction in directions:
                    check = (direction[0] + x, direction[1] + y)
                    if check[0] >= 0 and check[1] >= 0 and check[1] < len(mapdata) and check[0] < len(mapdata[0]) and mapdata[check[1]][check[0]] in '.@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        graph.add_edge((x,y),check)
                        
    queue = PriorityQueue()
    queue.put([0, [], deepcopy(pos), (), 0])
    queue.put([0, [], deepcopy(pos), (), 1])
    queue.put([0, [], deepcopy(pos), (), 2])
    queue.put([0, [], deepcopy(pos), (), 3])

    seen = set()
    ways = {}


    while queue.qsize() > 0:
        item = queue.get()
        if len(item[1]) == len(keys):
            return item[0]
        seen.add(item[3])
        for key, keyloc in keys.items():
            if key not in item[1]:
                way = None
                if (item[2][item[4]], keyloc) in ways:
                    way = ways[(item[2][item[4]], keyloc)]
                else:
                    way = []
                    if nx.has_path(graph, item[2][item[4]], keyloc):
                        way = nx.shortest_path(graph, item[2][item[4]], keyloc)
                    ways[(item[2][item[4]], keyloc)] = way
                    ways[(keyloc, item[2][item[4]])] = [way[-x-1] for x in range(len(way))]

                if len(way) == 0:
                    continue

                has_needed_keys = True
                for lock in locks:
                    if lock in way and chr(ord(locks[lock])+32) not in item[1]:
                        has_needed_keys = False
                        break
                for not_obtained_key in [x for x in keys if x not in item[1] and x != key]:
                    if keys[not_obtained_key] in way:
                        has_needed_keys = False
                        break
                if has_needed_keys:
                    new_keys = copy(item[1])
                    new_keys.append(key)
                    newpos = deepcopy(item[2])
                    newpos[item[4]] = way[-1]
                    for xx in range(4):
                        check = tuple([tuple(sorted(copy(new_keys)))] + [tuple(newpos), xx])
                        if check not in seen:
                            seen.add(check)
                            queue.put([item[0] + len(way) - 1, copy(new_keys), newpos, check, xx])

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_shortest(data)

    # Part 2
    solution2 = find_shortest2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

def tools():
    print('map example:')
    #import networkx as nx
    #import matplotlib.pyplot as plt
    #graph.add_edge((0,1),(1,1))
    #graph.add_edge((1,0),(1,1))
    #nx.shortest_path(graph, (0,0), (1,0))
    #nx.draw(graph, pos={x:x for x in graph.nodes}, with_labels=True)
    #plt.show()

    print('numpy:')
    #import numpy as np
    #np.lcm(1,2)
    #np.lcm.reduce([1,2,3,4])
