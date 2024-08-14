"""
Solution for day 24 of year 2017
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([int(x) for x in line.strip().split('/')])

def get_strongest(data, has_to_be_longest = False):
    strongest = -1
    length = -1
    queue = [[0, 0, deepcopy(list(data)), 0]]

    while len(queue) > 0:
        item = queue.pop(0)
        for i in range(len(item[2])):
            if item[2][i][0] == item[1]:
                new_list = deepcopy(item[2])
                del new_list[i]
                new_item = [item[0] + item[2][i][0] + item[2][i][1], item[2][i][1], new_list, item[3] + 1]
                queue.append(new_item)
            elif item[2][i][1] == item[1]:
                new_list = deepcopy(item[2])
                del new_list[i]
                new_item = [item[0] + item[2][i][0] + item[2][i][1], item[2][i][0], new_list, item[3] + 1]
                queue.append(new_item)
        if has_to_be_longest:
            if item[3] > length or (item[3] == length and item[0] > strongest):
                length = item[3]
                strongest = item[0]
        else:
            if item[0] > strongest:
                strongest = item[0]
    return strongest

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_strongest(data)

    # Part 2
    solution2 = get_strongest(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

