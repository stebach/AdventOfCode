"""
Solution for day 08 of year 2018
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_line(inputdata.read().strip())[1]

def list_to_nodes(data):
    result = [
        [],
        []
    ]

    subnodes = data[0]
    metadata = data[1]
    data = data[2:]
    while subnodes > len(result[0]):
        data, subnode = list_to_nodes(data)
        result[0] = result[0] + [subnode]
    if metadata > 0:
        result[1] = data[:metadata]
        data = data[metadata:]
    return data, result

def parse_line(line):
    data = list(map(int, line.strip().split(" ")))
    return list_to_nodes(data)

def sum_metadata(data):
    total = 0
    for sub in data[0]:
        total = total + sum_metadata(sub)
    return total + sum(data[1])


def part1(data):
    """Solve part 1"""
    return sum_metadata(data)

def calc_node_value(data):
    if len(data[0]) == 0:
        return sum(data[1])
    total = 0
    for idx in [x - 1 for x in data[1]]:
        if idx > -1 and idx < len(data[0]):
            total = total + calc_node_value(data[0][idx])
    return total

def part2(data):
    """Solve part 2"""
    return calc_node_value(data)

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
