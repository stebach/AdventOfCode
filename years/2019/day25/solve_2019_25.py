"""
Solution for day 25 of year 2019
"""

import os
import regex
from copy import deepcopy
import networkx as nx


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
    output = []
    graph = nx.Graph()
    directions = {
        'north': (0,-1),
        'south': (0,1),
        'east': (1,0),
        'west': (-1,0)
    }
    pointer = 0
    base = 0
    unexplored = []
    current_node = (0,0,"")
    check_room = None
    pre_check_room = None
    check_room_direction = None
    while len(unexplored) > 0 or len(graph.nodes) == 0:
        input = []
        output = []
        skipdirection = ''
        last_node = current_node
        if len(unexplored) > 0:
            next_node = unexplored.pop()
            way = nx.shortest_path(graph, current_node, next_node)
            way.pop(0)
            for step in way:
                if step[1] + 1 == current_node[1]:
                    input += [ord(x) for x in [*'north\n']]
                    skipdirection = 'south'
                elif step[1] - 1 == current_node[1]:
                    input += [ord(x) for x in [*'south\n']]
                    skipdirection = 'north'
                elif step[0] + 1 == current_node[0]:
                    input += [ord(x) for x in [*'west\n']]
                    skipdirection = 'east'
                elif step[0] - 1 == current_node[0]:
                    input += [ord(x) for x in [*'east\n']]
                    skipdirection = 'west'
                current_node = step
        pointer, base = intcode(data,input,output, pointer, base)
        text = "".join([chr(x) for x in output])
        print(text)
        if 'Pressure-Sensitive Floor' in text:
            check_room = current_node
            current_node = last_node
            pre_check_room = current_node
            if check_room[1] + 1 == pre_check_room[1]:
                check_room_direction= [ord(x) for x in [*'north\n']]
            elif check_room[1] - 1 == pre_check_room[1]:
                check_room_direction= [ord(x) for x in [*'south\n']]
            elif check_room[0] + 1 == pre_check_room[0]:
                check_room_direction= [ord(x) for x in [*'west\n']]
            elif check_room[0] - 1 == pre_check_room[0]:
                check_room_direction= [ord(x) for x in [*'east\n']]
        options = regex.findall('- ([^\n]+)\n',text.split("==")[-1])
        for option in options:
            if option in directions:
                if option not in skipdirection:
                    pos = (current_node[0] + directions[option][0], current_node[1] + directions[option][1], current_node[2] + option[0])
                    if pos not in graph.nodes:
                        unexplored.append(pos)
                    graph.add_edge(current_node, pos)
            elif option not in ['escape pod','molten lava','giant electromagnet','photons','infinite loop']:
                output = []
                input = [ord(x) for x in [*'take ' + option + '\n']]
                pointer, base = intcode(data,input,output, pointer, base)
                text = "".join([chr(x) for x in output])
                print(text)

    input = []
    output = []
    way = nx.shortest_path(graph, current_node, pre_check_room)
    way.pop(0)
    for step in way:
        if step[1] + 1 == current_node[1]:
            input += [ord(x) for x in [*'north\n']]
            skipdirection = 'south'
        elif step[1] - 1 == current_node[1]:
            input += [ord(x) for x in [*'south\n']]
            skipdirection = 'north'
        elif step[0] + 1 == current_node[0]:
            input += [ord(x) for x in [*'west\n']]
            skipdirection = 'east'
        elif step[0] - 1 == current_node[0]:
            input += [ord(x) for x in [*'east\n']]
            skipdirection = 'west'
        current_node = step
    pointer, base = intcode(data,input,output, pointer, base)
    text = "".join([chr(x) for x in output])
    print(text)


    output = []
    input += [ord(x) for x in [*'inv\n']]
    pointer, base = intcode(data,input,output, pointer, base)
    text = "".join([chr(x) for x in output])
    print(text)
    options = regex.findall('- ([^\n]+)\n',text)
    
    print(options)

    for i in range(pow(2,len(options))):
        input = []
        for j in range(len(options)):
            if i & pow(2,j) > 0:
                input += [ord(x) for x in [*'take ' + options[j] + '\n']]
            else:
                input += [ord(x) for x in [*'drop ' + options[j] + '\n']]

        output = []
        input += deepcopy(check_room_direction)
        pointer, base = intcode(data,input,output, pointer, base)
        text = "".join([chr(x) for x in output])
        if not 'Alert!' in text:
            print(text)
            exit()

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
