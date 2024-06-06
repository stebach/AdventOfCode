"""
Solution for day 21 of year 2016
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().split(' ')
    if line[0] == 'swap' and line[1] == 'position':
        return ('swap position', int(line[2]), int(line[5]))
    elif line[0] == 'swap' and line[1] == 'letter':
        return ('swap letter', line[2], line[5])
    elif line[0] == 'reverse' and line[1] == 'positions':
        return ('reverse positions', int(line[2]), int(line[4]))
    elif line[0] == 'rotate' and (line[1] == 'left' or line[1] == 'right'):
        return ('rotate', line[1], int(line[2]))
    elif line[0] == 'move' and line[1] == 'position':
        return ('move position', int(line[2]), int(line[5]))
    elif line[0] == 'rotate' and line[1] == 'based':
        return ('rotate based on position', line[6])
    print(line)
    exit()

def scramble(password, data, unscramble = False):
    password = [*password]
    if unscramble:
        data = data[::-1]
    for row in data:
        if row[0] == 'swap position':
            tmp = password[row[1]]
            password[row[1]] = password[row[2]]
            password[row[2]] = tmp
        elif row[0] == 'swap letter':
            password = [row[1] if x == row[2] else row[2] if x == row[1] else x for x in password]
        elif row[0] == 'reverse positions':
            password = password[:row[1]] + password[row[1]:row[2]+1][::-1] + password[row[2] + 1:]
        elif row[0] == 'rotate':
            if (row[1] == 'left' and not unscramble) or (row[1] == 'right' and unscramble) :
                password = password[(row[2]%len(password)):] + password[:(row[2]%len(password))]
            else:
                password = password[-(row[2]%len(password)):] + password[:-(row[2]%len(password))]
        elif row[0] == 'move position':
            if unscramble:
                tmp = password.pop(row[2])
                password.insert(row[1], tmp)
            else:
                tmp = password.pop(row[1])
                password.insert(row[2], tmp)
        elif row[0] == 'rotate based on position':
            if unscramble:
                for x in range(1, len(password)):
                    tmp = password[x:] + password[:x]
                    idx = tmp.index(row[1]) + 1
                    if idx > 4:
                        idx += 1
                    idx = idx % len(password)
                    check = tmp[-idx:] + tmp[:-idx]
                    if check == password:
                        password = tmp
                        break
            else:
                idx = password.index(row[1]) + 1
                if idx > 4:
                    idx += 1
                idx = idx % len(password)

                password = password[-idx:] + password[:-idx]
        else:
            print(row)
            exit()
    return "".join(password)


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = scramble('abcdefgh', data)

    # Part 2
    solution2 = scramble('fbgdceah', data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

