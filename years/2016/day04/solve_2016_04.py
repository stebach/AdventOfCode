"""
Solution for day 04 of year 2016
"""

import os
import regex
from queue import PriorityQueue

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = regex.findall(r'^(.*)\-([0-9]+)\[([a-z]{5})\]', line.strip())
    return (line[0][0], int(line[0][1]), line[0][2])

def is_real_room(data):
    ordered_chars = PriorityQueue()
    teststring = data[0]
    while len(teststring) > 0:
        char = teststring[0]
        if char != '-':
            ordered_chars.put((-teststring.count(char), char))
        teststring = teststring.replace(char, '')
    check = ''
    while len(check) < 5:
        check += ordered_chars.get()[1]
    return check == data[2]

def decrypt(data):
    return ''.join([' ' if ord(x) == 45 else chr(((ord(x) - 97) + data[1]) % 26 + 97) for x in [*data[0]]])

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum([x[1] for x in data if is_real_room(x)])

    # Part 2
    solution2 = [x[1] for x in data if is_real_room(x) and decrypt(x).count('north') > 0 and decrypt(x).count('pole') > 0 and decrypt(x).count('object') > 0][0]

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

