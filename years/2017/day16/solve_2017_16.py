"""
Solution for day 16 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    parts = lines[0].split(',')
    result = []
    for part in parts:
        if part[0] == 's':
            result.append(('s', int(part[1:])))
        elif part[0] == 'x':
            result.append(tuple(['x'] + [int(x) for x in part[1:].split('/')]))
        elif part[0] == 'p':
            result.append(tuple(['p'] + part[1:].split('/')))
        else:
            print("unknown type: " + part[0])
            exit()
    return tuple(result)

def dance(data, keys = 16, programs = {}, get_object = False):

    if len(programs) == 0:
        for key in range(keys):
            programs[chr(97+key)] = key

    for step in data:
        if step[0] == 's':
            for x in programs.keys():
                programs[x] = (programs[x] + step[1]) % keys
        elif step[0] == 'x':
            for x in programs.keys():
                if programs[x] == step[1]:
                    programs[x] = step[2]
                elif programs[x] == step[2]:
                    programs[x] = step[1]
        elif step[0] == 'p':
            tmp = programs[step[1]]
            programs[step[1]] = programs[step[2]]
            programs[step[2]] = tmp
        else:
            print("unknown type: " + step[0])
            exit()

    if get_object:
        return programs

    out = [''] * keys
    for x in programs.items():
        out[x[1]] = x[0]
    return ''.join(out)

def dance_repeat(data, keys, repeats):
    programs = {}
    for key in range(keys):
        programs[chr(97+key)] = key
    cachekey = "|".join(list([x[0] + "_" + str(x[1]) for x in programs.items()]))
    seen = [cachekey]
    for x in range(repeats):
        programs = dance(data, keys, programs, True)
        cachekey = "|".join(list([x[0] + "_" + str(x[1]) for x in programs.items()]))
        if cachekey not in seen:
            seen.append(cachekey)
        else:
            break
    repeats_list = seen[seen.index(cachekey):]
    final = repeats_list[(repeats - x - 1) % len(repeats_list)]
    programs = dict([x.split('_') for x in final.split('|')])

    out = [''] * keys
    for x in programs.items():
        out[int(x[1])] = x[0]
    return ''.join(out)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = dance(data)

    # Part 2
    solution2 = dance_repeat(data, 16, 1_000_000_000)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

