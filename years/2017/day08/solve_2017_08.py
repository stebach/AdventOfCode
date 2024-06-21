"""
Solution for day 08 of year 2017
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    result = regex.findall(r'([^ ]+) (inc|dec) (-?[0-9]+) if ([^ ]+) ([<=>!]+) (-?[0-9]+)',line.strip())
    if len(result) != 1:
        print("ERR:")
        print(result)
        print(line)
    return (result[0][0], result[0][1], int(result[0][2]), result[0][3], result[0][4], int(result[0][5]))

def get_max(data, return_highest_ever = False):
    result = {}
    highest_ever = 0
    for cmd in data:
        mod = cmd[2]
        if cmd[1] == 'dec':
            mod *= -1
        if cmd[0] not in result:
            result[cmd[0]] = 0
        if cmd[3] not in result:
            result[cmd[3]] = 0
        if do_comparison(result[cmd[3]], cmd[4], cmd[5]):
            result[cmd[0]] += mod
            if result[cmd[0]] > highest_ever:
                highest_ever = result[cmd[0]]
    if return_highest_ever:
        return highest_ever
    return max([result[x] for x in result])

def do_comparison(val1, operator, val2):
        if operator == '>':
            return val1 > val2
        elif operator == '<':
            return val1 < val2
        elif operator == '>=':
            return val1 >= val2
        elif operator == '==':
            return val1 == val2
        elif operator == '<=':
            return val1 <= val2
        elif operator == '!=':
            return val1 != val2
        else:
            print("UNKNOWN COMPARISON:")
            print(operator)
            exit()


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_max(data)

    # Part 2
    solution2 = get_max(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

