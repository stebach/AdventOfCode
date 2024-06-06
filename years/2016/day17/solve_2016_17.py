"""
Solution for day 17 of year 2016
"""

import os
from queue import PriorityQueue
from hashlib import md5

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read().strip()

def find_path(passcode, longest = False):
    pos = (0,0)
    width = 4
    height = 4
    goal = (3, 3)
    queue = PriorityQueue()
    queue.put((0, pos, passcode))
    directions = ((0,-1),(0,1),(-1,0),(1,0))

    longest_len = 0

    while queue.qsize() > 0:
        check = queue.get()
        hash = md5(check[2].encode()).hexdigest()
        for idx, direction in enumerate(directions):
            nextpos = (check[1][0] + direction[0], check[1][1] + direction[1])
            if -1 in nextpos or nextpos[0] >= width or nextpos[1] >= height:
                continue
            if hash[idx] in 'bcdef':
                newpasscode = check[2] + 'UDLR'[idx]
                if nextpos == goal:
                    if longest:
                        if len(newpasscode) - len(passcode) > longest_len:
                            longest_len = len(newpasscode) - len(passcode)
                        continue
                    else:
                        return newpasscode[len(passcode):]
                queue.put((check[0] + 1, nextpos, newpasscode))
    
    if longest:
        return longest_len

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_path(data)

    # Part 2
    solution2 = find_path(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
