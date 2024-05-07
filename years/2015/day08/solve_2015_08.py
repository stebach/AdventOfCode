"""
Solution for day 08 of year 2015
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def num_memory(data):
    return len(data)

def num_literal(data):
    return len(unescape(data))

def unescape(data):
    data = data[1:-1]
    matches = regex.finditer(r'(\\\\|\\"|\\x[0-9a-fA-F]{2})', data)
    delta = 0
    for x in matches:
        if x.group() == '\\"':
            data = data[0:x.span()[0] - delta] + '"' + data[x.span()[1] - delta:]
            delta += 1
        elif x.group() == '\\\\':
            data = data[0:x.span()[0] - delta] + '\\' + data[x.span()[1] - delta:]
            delta += 1
        else:
            data = data[0:x.span()[0] - delta] + '|' + data[x.span()[1] - delta:]
            delta += 3
    return data

def num_escaped(data):
    return len("".join([('\\' if x in ['\\','\"'] else "") + x for x in data])) + 2

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum([num_memory(x) - num_literal(x) for x in data])

    solution2 = sum([num_escaped(x) - num_memory(x) for x in data])

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
