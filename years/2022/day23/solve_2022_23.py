"""
Solution for day 23 of year 2022
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                result.append((x,y))
    return tuple(result)

def move_elfs(data, rounds = 1_000_000):
    order = [(0,-1),(0,1),(-1,0),(1,0)]
    order_check = {
        (0,-1): ((1,-1),(0,-1),(-1,-1)),
        (0,1): ((1,1),(0,1),(-1,1)),
        (-1,0): ((-1,1),(-1,0),(-1,-1)),
        (1,0): ((1,1),(1,0),(1,-1))
    }
    elfs = deepcopy(data)

    roundNo = 0
    for i in range(rounds):
        roundNo += 1
        moved = False
        elfs_new = {}
        for elf in elfs:
            count = 0
            for y in range(3):
                for x in range(3):
                    if (x - 1 + elf[0], y - 1 + elf[1]) in elfs:
                        count += 1
                        if count > 1:
                            break
                if count > 1:
                    break
            target = elf
            if count > 1:
                for direction in order:
                    go = True
                    for direction_check in order_check[direction]:
                        if (elf[0] + direction_check[0], elf[1] + direction_check[1]) in elfs:
                            go = False
                            break
                    if go:
                        target = (elf[0] + direction[0], elf[1] + direction[1])
                        break
            if not target in elfs_new:
                elfs_new[target] = []
            elfs_new[target].append(elf)

        tmp = []
        for e in elfs_new:
            if len(elfs_new[e]) > 1:
                tmp += elfs_new[e]
            else:
                if e != elfs_new[e][0]:
                    moved = True
                tmp.append(e)
        elfs = tuple(tmp)
        order.append(order.pop(0))
        if not moved:
            break

    elfs_x = [x[0] for x in elfs]
    elfs_y = [y[1] for y in elfs]
    return (
        (max(elfs_x) - min(elfs_x) + 1) * (max(elfs_y) - min(elfs_y) + 1) - len(elfs),
        roundNo
    )

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = move_elfs(data, 10)[0]

    # Part 2
    solution2 = move_elfs(data)[1]

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

