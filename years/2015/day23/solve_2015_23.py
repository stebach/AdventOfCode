"""
Solution for day 23 of year 2015
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().replace(', ', ' ').split(' ')
    if line[0] == 'jmp':
        return (line[0], int(line[1]))
    elif line[0] == 'jie' or line[0] == 'jio':
        return (line[0], line[1], int(line[2]))
    else:
        return (line[0], line[1])

def run(data, a_start = 0):
    result = { 'a': a_start, 'b': 0}

    idx = 0
    while idx < len(data):
        if data[idx][0] == 'hlf':
            result[data[idx][1]] //= 2
            idx += 1
        elif data[idx][0] == 'tpl':
            result[data[idx][1]] *= 3
            idx += 1
        elif data[idx][0] == 'inc':
            result[data[idx][1]] += 1
            idx += 1
        elif data[idx][0] == 'jmp':
            idx += data[idx][1]
        elif data[idx][0] == 'jie':
            if result[data[idx][1]] % 2 == 0:
                idx += data[idx][2]
            else:
                idx += 1
        elif data[idx][0] == 'jio':
            if result[data[idx][1]] == 1:
                idx += data[idx][2]
            else:
                idx += 1
        else:
            print("ERR: unknown command: " + data[idx][0])
            exit()

    return result

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = run(data)['b']

    # Part 2
    solution2 = run(data, 1)['b']

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
