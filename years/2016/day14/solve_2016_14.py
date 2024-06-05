"""
Solution for day 14 of year 2016
"""

import os
from hashlib import md5
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read()

def find_keys(data, stretched = False):
    result = []
    idx = 0
    index3 = {}

    while len(result) < 64:
        hash = md5((data+str(idx)).encode()).hexdigest()
        if stretched:
            for x in range(2016):
                hash = md5(hash.encode()).hexdigest()
        match3 = regex.findall(r'([a-f0-9])\1\1', hash)
        match5 = regex.findall(r'([a-f0-9])\1\1\1\1', hash)
        if len(match5) > 0:
            validkeys = [x for x in index3 if index3[x][0] == match5[0] and index3[x][1] == False]
            for idx2 in validkeys:
                index3[idx2][1] = True
        if len(match3) > 0:
            index3[idx] = [match3[0], False]
        if idx - 1000 in index3:
            if index3[idx - 1000][1]:
                result.append((idx - 1000, index3[idx - 1000][0]))
            del index3[idx - 1000]
        idx += 1
    return result

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_keys(data)[63][0]

    # Part 2
    solution2 = find_keys(data, True)[63][0]

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
