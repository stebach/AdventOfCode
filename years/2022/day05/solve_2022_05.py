"""
Solution for day 05 of year 2022
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    crates = []
    while len(lines) > 0:
        line = lines.pop(0)
        if line[0:2] == ' 1':
            lines.pop(0)
            break
        for (pos, char) in enumerate(line):
            if char == '[':
                idx = int(pos/4)
                while len(crates) < idx + 1:
                    crates.append([])
                crates[idx].append(line[pos+1])
    
    for col in range(len(crates)):
        crates[col] = crates[col][::-1]

    moves = []
    while len(lines) > 0:
        line = lines.pop(0).strip().split(' ')
        moves.append(tuple([int(line[1]), int(line[3]) - 1, int(line[5]) - 1]))

    return (crates, tuple(moves))

def move(data, multiple = False):
    data = deepcopy(data)
    for next_move in data[1]:
        buffer = []
        for i in range(next_move[0]):
            buffer.append(data[0][next_move[1]].pop())
        while len(buffer) > 0:
            if multiple:
                data[0][next_move[2]].append(buffer.pop())
            else:
                data[0][next_move[2]].append(buffer.pop(0))
    return "".join([x[-1] for x in data[0]])

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = move(data)

    # Part 2
    solution2 = move(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

