"""
Solution for day 17 of year 2019
"""

import os
from copy import deepcopy
import re

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

def get_alignment_parameters(data):
    result = 0
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col == '#' and x > 0 and y > 0 and x < len(row) - 1 and y < len(data) -1:
                if data[y-1][x] == '#' and data[y+1][x] == '#' and data[y][x-1] == '#' and data[y][x+1] == '#':
                    result += x * y

    return result

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    output = []
    intcode(deepcopy(data),[],output)
    map = "".join([chr(x) for x in output]).strip().split('\n')

    solution1 = get_alignment_parameters(map)

    # Part 2
    current_direction = (0,0)
    current_pos = (0,0)
    for y, row in enumerate(map):
        for x, col in enumerate(row):
            if col in '<^v>':
                current_pos = (x,y)
                if col == '<':
                    current_direction = (-1,0)
                elif col == '>':
                    current_direction = (1,0)
                elif col == '^':
                    current_direction = (0,-1)
                elif col == 'v':
                    current_direction = (0,1)
    instructions = []
    while True:
        next_pos = (current_pos[0] + current_direction[0], current_pos[1] + current_direction[1])
        if not is_valid(next_pos, map) or map[next_pos[1]][next_pos[0]] != '#':
            left = (current_direction[1],-current_direction[0])
            left_pos = (current_pos[0] + left[0], current_pos[1] + left[1])
            right = (-current_direction[1], current_direction[0])
            right_pos = (current_pos[0] + right[0], current_pos[1] + right[1])
            if is_valid(left_pos, map) and map[left_pos[1]][left_pos[0]] == '#':
                instructions.append("L,")
                instructions.append("1")
                current_pos = left_pos
                current_direction = left
            elif is_valid(right_pos, map) and map[right_pos[1]][right_pos[0]] == '#':
                instructions.append("R,")
                instructions.append("1")
                current_pos = right_pos
                current_direction = right
            else:
                break
        else:
            current_pos = next_pos
            instructions.append("1")
    
    instruction_string = "".join(instructions)
    for i in range(0, 20, 2):
        instruction_string = instruction_string.replace('1' * (20 - i), str(20 - i))
    instructions = [x for x in re.findall(r'[LR],\d+', instruction_string)]
    
    instructions_orig = deepcopy(instructions)

    dict = {}
    current_char = 65
    while not all(x in list(dict) for x in instructions):
        dict[chr(current_char)] = []
        pos = 0
        while pos < len(instructions) and instructions[pos] in list(dict):
            pos += 1
        while pos < len(instructions) and len(','.join(dict[chr(current_char)])) + len(instructions[pos]) < 20 and instructions[pos] not in list(dict):
            dict[chr(current_char)].append(instructions[pos])
            pos += 1

        replace_in_list(instructions, dict[chr(current_char)], [chr(current_char)])

        check_last_len(instructions, dict, current_char)

        while chr(current_char) not in list(dict):
            current_char -= 1

        current_char += 1

    input_string = []
    input_string.append(','.join(instructions))
    for x in dict:
        input_string.append(','.join(dict[x]))
    input_string = "\n".join(input_string) + "\n\n\n"
    input = [ord(x) for x in input_string]
    output = []
    data[0] = 2
    intcode(data,input,output)
    solution2 = output[-1]

    return solution1, solution2

def replace_in_list(the_list, search, replacement):
    pos = 0
    while pos + len(search) <= len(the_list):
        if the_list[pos:pos+len(search)] == search:
            the_list[pos:pos+len(search)] = replacement
        pos += 1

def check_last_len(instructions, dict, current_char):
    if len(dict[chr(current_char)]) < 3 or current_char >= 68:
        replace_in_list(instructions, [chr(current_char)], dict[chr(current_char)])
        del dict[chr(current_char)]
        if current_char > 65:
            replace_in_list(instructions, [chr(current_char - 1)], [chr(current_char - 1), dict[chr(current_char-1)][-1]])
            dict[chr(current_char - 1)].pop()
            replace_in_list(instructions, dict[chr(current_char - 1)], [chr(current_char - 1)])
            check_last_len(instructions, dict, current_char - 1)



def is_valid(pos, map):
    return not (pos[0] < 0 or pos[1] < 0 or pos[0] >= len(map[0]) or pos[1] >= len(map))

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

def tools():
    print('map example:')
    #import networkx as nx
    #import matplotlib.pyplot as plt
    #map = nx.Graph()
    #map.add_edge((0,0),(0,1))
    #map.add_edge((0,1),(1,1))
    #map.add_edge((1,0),(1,1))
    #nx.shortest_path(map, (0,0), (1,0))
    #nx.draw(map, pos={x:x for x in map.nodes}, with_labels=True)
    #plt.show()

    print('numpy:')
    #import numpy as np
    #np.lcm(1,2)
    #np.lcm.reduce([1,2,3,4])
