"""
Solution for day 23 of year 2020
"""

import os
from copy import copy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        # run lines through function
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    return sum([[int(y) for y in [*(x.strip())]] for x in lines],[])

def do_moves(data, moves, fill=0):
    localdata = copy(data)
    next_val = max(localdata) + 1
    while len(localdata) < fill:
        localdata.append(next_val)
        next_val += 1
    next = {}
    for pos, nr in enumerate(localdata):
        next[nr] = pos + 1
        if pos + 1 == len(localdata):
            next[nr] = 0
    
    idx = 0
    for move in range(moves):
        number = localdata[idx]
        movedata = []
        for i in range(3):
            movedata.append(next[number])
            number = localdata[next[number]]

        next[localdata[idx]] = next[number]
        target_number = localdata[idx] - 1
        while target_number < 1 or localdata[movedata[0]] == target_number or localdata[movedata[1]] == target_number or localdata[movedata[2]] == target_number:
            target_number -= 1
            if target_number < 1:
                target_number = len(localdata)
        
        next[localdata[movedata[2]]] = next[target_number]
        next[target_number] = movedata[0]

        idx = next[localdata[idx]]

    result = []
    pos = next[1]
    for i in range(8):
        num = localdata[pos]
        pos = next[num]
        result.append(num)

    return result


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = "".join([str(x) for x in do_moves(data, 100)])

    # Part 2
    result = do_moves(data, 10_000_000, 1_000_000)
    solution2 = result[0] * result[1]
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

