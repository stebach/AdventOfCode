"""
Solution for day 07 of year 2019
"""

import os
from math import floor
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return [int(x) for x in inputdata.read().split(',')]

def parse_line(line):
    return line.strip()

def parse_lines(lines):
    return [x for x in lines]

def intcode(data, input = [], output = [], pointer = 0):
    while data[pointer] != 99:
        opcode = data[pointer] % 100
        if opcode == 1:
            data[data[pointer+3]] = intcode_get_param(1,data,pointer) + intcode_get_param(2,data,pointer)
            pointer += 4
        elif opcode == 2:
            data[data[pointer+3]] = intcode_get_param(1,data,pointer) * intcode_get_param(2,data,pointer)
            pointer += 4
        elif opcode == 3:
            if len(input) == 0:
                return pointer
            data[data[pointer+1]] = input.pop(0)
            pointer += 2
        elif opcode == 4:
            output.append(intcode_get_param(1,data,pointer))
            pointer += 2
        elif opcode == 5:
            if intcode_get_param(1,data,pointer) != 0:
                pointer = intcode_get_param(2,data,pointer)
            else:
                pointer += 3
        elif opcode == 6:
            if intcode_get_param(1,data,pointer) == 0:
                pointer = intcode_get_param(2,data,pointer)
            else:
                pointer += 3
        elif opcode == 7:
            if intcode_get_param(1,data,pointer) < intcode_get_param(2,data,pointer):
                data[data[pointer+3]] = 1
            else:
                data[data[pointer+3]] = 0
            pointer += 4
        elif opcode == 8:
            if intcode_get_param(1,data,pointer) == intcode_get_param(2,data,pointer):
                data[data[pointer+3]] = 1
            else:
                data[data[pointer+3]] = 0
            pointer += 4
        else:
            print (data)
            print("ERR: UNKNOWN OPCODE: " + str(data[pointer]))
            exit()
    return pointer

def intcode_get_param(no, data, pointer):
    mode = 0
    if data[pointer] >= pow(10,1+no):
        tostr = str(data[pointer])
        mode = int(tostr[len(tostr)-2-no])
    if mode == 0:
        return data[data[pointer+no]]
    else:
        return data[pointer+no]

def run_amplifiers(a,b,c,d,e,data):
    data1 = deepcopy(data)
    data2 = deepcopy(data)
    data3 = deepcopy(data)
    data4 = deepcopy(data)
    data5 = deepcopy(data)
    output = []
    intcode(data1, [a,0], output)
    intcode(data2, [b, output[-1]], output)
    intcode(data3, [c, output[-1]], output)
    intcode(data4, [d, output[-1]], output)
    intcode(data5, [e, output[-1]], output)
    return output[-1]

def run_amplifiers_advanced(a,b,c,d,e,data):
    data1 = deepcopy(data)
    data2 = deepcopy(data)
    data3 = deepcopy(data)
    data4 = deepcopy(data)
    data5 = deepcopy(data)
    output = [0]
    pointer1 = 0
    pointer2 = 0
    pointer3 = 0
    pointer4 = 0
    pointer5 = 0

    input1 = [a]
    input2 = [b]
    input3 = [c]
    input4 = [d]
    input5 = [e]

    while data5[pointer5] != 99:
        input1.append(output[-1])
        pointer1 = intcode(data1, input1, output, pointer1)
        input2.append(output[-1])
        pointer2 = intcode(data2, input2, output, pointer2)
        input3.append(output[-1])
        pointer3 = intcode(data3, input3, output, pointer3)
        input4.append(output[-1])
        pointer4 = intcode(data4, input4, output, pointer4)
        input5.append(output[-1])
        pointer5 = intcode(data5, input5, output, pointer5)
    return output[-1]


def part1(data):
    """Solve part 1"""
    max_val = 0
    for a in range(5):
        for b in range(5):
            if b == a:
                continue
            for c in range(5):
                if c in [a, b]:
                    continue
                for d in range(5):
                    if d in [a, b, c]:
                        continue
                    for e in range(5):
                        if e in [a, b, c, d]:
                            continue
                        max_val = max(max_val, run_amplifiers(a,b,c,d,e, data))
    return max_val

def part2(data):
    """Solve part 2"""
    max_val = 0
    for a in range(5):
        for b in range(5):
            if b == a:
                continue
            for c in range(5):
                if c in [a, b]:
                    continue
                for d in range(5):
                    if d in [a, b, c]:
                        continue
                    for e in range(5):
                        if e in [a, b, c, d]:
                            continue
                        max_val = max(max_val, run_amplifiers_advanced(a+5,b+5,c+5,d+5,e+5, data))
    return max_val

def draw_map():
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


def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
