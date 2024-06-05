"""
Solution for day 12 of year 2016
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().split(' ')
    if line[0] == 'cpy':
        if line[1] in 'abcd':
            return ('cpyz', ord(line[1]) - 97, ord(line[2]) - 97)
        else:
            return ('cpy', int(line[1]), ord(line[2]) - 97)
    elif line[0] == 'inc':
        return ('inc', ord(line[1]) - 97)
    elif line[0] == 'dec':
        return ('dec', ord(line[1]) - 97)
    elif line[0] == 'jnz':
        return ('jnz', ord(line[1]) - 97, int(line[2]))
    else:
        print('UNKNOWN CMMAND ' + line[0])
        print(line)
        exit()

def run(data, initial_c = 0):
    result = [0, 0, initial_c, 0]
    idx = 0

    while idx < len(data):
        cmd = data[idx]
        if cmd[0] == 'cpy':
            result[cmd[2]] = cmd[1]
        elif cmd[0] == 'cpyz':
            result[cmd[2]] = result[cmd[1]]
        elif cmd[0] == 'inc':
            result[cmd[1]] += 1
        elif cmd[0] == 'dec':
            result[cmd[1]] -= 1
        elif cmd[0] == 'jnz':
            if cmd[1] < 0:
                if cmd[1] != -49:
                    idx += cmd[2] - 1
            elif result[cmd[1]] != 0:
                idx += cmd[2] - 1
        else:
            print("UNKNOWN COMMAND: " + cmd[0])
            exit()
        idx += 1
    return result

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = run(data)[0]

    # Part 2
    solution2 = run(data, 1)[0]

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
