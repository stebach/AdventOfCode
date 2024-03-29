"""
Solution for day 12 of year 2021
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    paths = {}
    small = []
    for line in lines:
        line = line.strip().split('-')
        if not line[0] in paths:
            paths[line[0]] = []
        if not line[1] in paths:
            paths[line[1]] = []
        paths[line[0]].append(line[1])
        paths[line[1]].append(line[0])
        if line[0] not in ['start','end'] and line[0] not in small and ord(line[0][0]) > 90:
            small.append(line[0])
        if line[1] not in ['start','end'] and line[1] not in small and ord(line[1][0]) > 90:
            small.append(line[1])
    return (
        paths,
        small
    )

def count_paths(data, allow_revisit = False):
    queue = [
        [['start'], False]
    ]
    count = 0

    while len(queue) > 0:
        check = queue.pop(0)
        for connection in data[0][check[0][-1]]:
            is_revisit = False
            if connection == 'start':
                continue
            if ord(connection[0]) > 90 and connection in check[0]:
                if not allow_revisit or check[1] is True:
                    continue
                else:
                    is_revisit = True
            if connection == 'end':
                count += 1
                continue
            c = deepcopy(check)
            c[0].append(connection)
            c[1] = is_revisit or c[1]
            queue.append(c)

    return count


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_paths(data)

    # Part 2
    solution2 = count_paths(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

