"""
Solution for day 08 of year 2025
"""

import os
import math

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().split(',')
    return tuple(map(int, line))

def connect(data, connections):
    circuits = {}
    circuit_no = 0
    junction_boxes = {}
    distances = []
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            d = math.dist(data[i], data[j])
            distances.append((d, i, j))
    distances.sort()

    connections_tried = 0
    while True:
        connections_tried += 1
        d, i, j = distances.pop(0)
        if i in junction_boxes and j in junction_boxes and junction_boxes[i] == junction_boxes[j]:
            continue
        if i in junction_boxes and j in junction_boxes:
            #merge
            to_remove = junction_boxes[j]
            for k in circuits[junction_boxes[j]]:
                circuits[junction_boxes[i]].add(k)
                junction_boxes[k] = junction_boxes[i]
            circuits.pop(to_remove)
        elif i in junction_boxes and j not in junction_boxes:
            #add j to i
            junction_boxes[j] = junction_boxes[i]
            circuits[junction_boxes[i]].add(j)
        elif j in junction_boxes and i not in junction_boxes:
            #add i to j
            junction_boxes[i] = junction_boxes[j]
            circuits[junction_boxes[j]].add(i)
        else:
            #new circuit
            junction_boxes[i] = circuit_no
            junction_boxes[j] = circuit_no
            circuits[circuit_no] = set([i, j])
            circuit_no += 1
        if connections_tried == connections:
            sorted_circuit_sizes = sorted([len(x) for x in circuits.values()], reverse=True)
            solution1 = sorted_circuit_sizes[0] * sorted_circuit_sizes[1] * sorted_circuit_sizes[2]
        elif len(circuits) == 1 and len(list(circuits.values())[0]) == len(data):
            solution2 = data[i][0] * data[j][0]
            break

    return solution1, solution2




def solve(data, connections_part1=1000):
    """Solve the puzzle for the given input"""

    solution1, solution2 = connect(data, connections_part1)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
