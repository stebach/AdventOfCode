"""
Solution for day 15 of year 2019
"""

import os
import networkx as nx
import matplotlib.pyplot as plt


def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return [int(x) for x in inputdata.read().split(',')]

def intcode(data, input = [], output = [], pointer = 0, relative_base = 0):
    while data[pointer] != 99:
        opcode = data[pointer] % 100
        if opcode == 1:
            index = intcode_get_index(3,data,pointer,relative_base)
            data[index] = data[intcode_get_index(1,data,pointer,relative_base)] + data[intcode_get_index(2,data,pointer,relative_base)]
            pointer += 4
        elif opcode == 2:
            index = intcode_get_index(3,data,pointer,relative_base)
            data[index] = data[intcode_get_index(1,data,pointer,relative_base)] * data[intcode_get_index(2,data,pointer,relative_base)]
            pointer += 4
        elif opcode == 3:
            if len(input) == 0:
                return pointer, relative_base
            index = intcode_get_index(1,data,pointer,relative_base)
            data[index] = input.pop(0)
            pointer += 2
        elif opcode == 4:
            output.append(data[intcode_get_index(1,data,pointer,relative_base)])
            pointer += 2
        elif opcode == 5:
            if data[intcode_get_index(1,data,pointer,relative_base)] != 0:
                pointer = data[intcode_get_index(2,data,pointer,relative_base)]
            else:
                pointer += 3
        elif opcode == 6:
            if data[intcode_get_index(1,data,pointer,relative_base)] == 0:
                pointer = data[intcode_get_index(2,data,pointer,relative_base)]
            else:
                pointer += 3
        elif opcode == 7:
            index = intcode_get_index(3,data,pointer,relative_base)
            if data[intcode_get_index(1,data,pointer,relative_base)] < data[intcode_get_index(2,data,pointer,relative_base)]:
                data[index] = 1
            else:
                data[index] = 0
            pointer += 4
        elif opcode == 8:
            index = intcode_get_index(3,data,pointer,relative_base)
            if data[intcode_get_index(1,data,pointer,relative_base)] == data[intcode_get_index(2,data,pointer,relative_base)]:
                data[index] = 1
            else:
                data[index] = 0
            pointer += 4
        elif opcode == 9:
            relative_base += data[intcode_get_index(1,data,pointer,relative_base)]
            pointer += 2
        else:
            print (data)
            print("ERR: UNKNOWN OPCODE: " + str(data[pointer]))
            exit()
    return pointer, relative_base

def intcode_get_index(no, data, pointer, relative_base):
    mode = 0
    if data[pointer] >= pow(10,1+no):
        tostr = str(data[pointer])
        mode = int(tostr[len(tostr)-2-no])
    index_to_return = pointer + no
    if mode == 0:
        index_to_return = data[pointer+no]
    elif mode == 2:
        index_to_return = relative_base + data[pointer+no]
    intcode_expand(data, index_to_return)
    return index_to_return

def intcode_expand(data, index):
    while index >= len(data):
        data.append(0)

def solve(data):
    """Solve the puzzle for the given input"""

    # Part 1
    pos = (0,0)
    unknown = [(0,1),(1,0),(-1,0)]
    visited = [(0,0), (0, -1)]
    last_direction = (0,-1)
    directions = {
        (0,-1): 1,
        (0, 1): 2,
        (-1,0): 3,
        (1, 0): 4
    }

    input=[1]
    output=[]
    graph = nx.Graph()
    graph.add_node((0,0))
    pointer, relative_base = intcode(data, input, output)
    target_pos = None
    while True:
        if output[-1] in [1,2]:
            pos = (pos[0] + last_direction[0], pos[1] + last_direction[1])
            if output[-1] == 2:
                target_pos = pos
            for direction in directions:
                to_check = (pos[0] + direction[0], pos[1] + direction[1])
                if to_check not in visited and to_check not in unknown:
                    unknown.append(to_check)
            to_add = []
            for node in graph.nodes:
                if abs(node[0] - pos[0]) + abs(node[1] - pos[1]) == 1:
                    to_add.append(node)
            for node in to_add:
                graph.add_edge(node, pos)
        if len(unknown) == 0:
            break
        min_distance = abs(unknown[0][0] - pos[0]) + abs(unknown[0][1] - pos[1])
        min_pos = unknown[0]
        for x in range(1, len(unknown)):
            distance = abs(unknown[x][0] - pos[0]) + abs(unknown[x][1] - pos[1])
            if distance < min_distance:
                min_distance = distance
                min_pos = unknown[x]
        if distance > 1:
            neighbour_node = None
            for node in graph.nodes:
                if abs(node[0] - min_pos[0]) + abs(node[1] - min_pos[1]) == 1:
                    neighbour_node = node
                    break
            path = nx.shortest_path(graph, pos, neighbour_node)
            for x in range(1, len(path)):
                last_direction = (path[x][0] - pos[0], path[x][1] - pos[1])
                input.append(directions[last_direction])
                pos = path[x]
        last_direction = (min_pos[0] - pos[0], min_pos[1] - pos[1])
        input.append(directions[last_direction])
        unknown.remove(min_pos)
        visited.append(min_pos)
        pointer, relative_base = intcode(data, input, output, pointer, relative_base)

    solution1 = nx.shortest_path_length(graph, (0,0), target_pos)

    # Part 2
    longest = 0
    for node in graph.nodes:
        if node != target_pos:
            longest = max(longest, nx.shortest_path_length(graph, target_pos, node))
    solution2 = longest
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
