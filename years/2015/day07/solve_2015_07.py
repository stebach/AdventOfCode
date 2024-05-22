"""
Solution for day 07 of year 2015
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return dict(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().split(' -> ')
    wire = line[0].split(' ')
    if len(wire) == 1:
        return (line[1], (wire[0],))
    elif len(wire) == 2:
        if wire[0] == 'NOT':
            return (line[1], ('NOT', wire[1]))
        else:
            print(wire)
            exit()
    elif len(wire) == 3:
        if wire[1] == 'AND':
            return (line[1], ('AND', wire[0], wire[2]))
        elif wire[1] == 'OR':
            return (line[1], ('OR', wire[0], wire[2]))
        elif wire[1] == 'LSHIFT':
            return (line[1], ('LSHIFT', wire[0], int(wire[2])))
        elif wire[1] == 'RSHIFT':
            return (line[1], ('RSHIFT', wire[0], int(wire[2])))
        else:
            print(wire)
            exit()
    print(line)
    return (line, 0)


def get_signals(data):
    result = {
    }

    for x in data:
        result[x] = get_wire_data(result, data, x)

    return result

    return result

def get_wire_data(result, data, x):
    if isinstance(x, int):
        return x
    if x.isdigit():
        return int(x)
    if not x in result:
        if len(data[x]) == 1:
            result[x] = get_wire_data(result, data, data[x][0])
        elif data[x][0] == 'AND':
            result[x] = (get_wire_data(result, data, get_wire_data(result, data, data[x][1])) & get_wire_data(result, data, data[x][2]))
        elif data[x][0] == 'OR':
            result[x] = (get_wire_data(result, data, get_wire_data(result, data, data[x][1])) | get_wire_data(result, data, data[x][2]))
        elif data[x][0] == 'LSHIFT':
            result[x] = (get_wire_data(result, data, get_wire_data(result, data, data[x][1])) << get_wire_data(result, data, data[x][2])) & 65535
        elif data[x][0] == 'RSHIFT':
            result[x] = (get_wire_data(result, data, get_wire_data(result, data, data[x][1])) >> get_wire_data(result, data, data[x][2])) & 65535
        elif data[x][0] == 'NOT':
            result[x] = (~get_wire_data(result, data, get_wire_data(result, data, data[x][1]))) & 65535
        else:
            print(data[x])
            exit()
    return result[x]


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_signals(data)['a']

    # Part 2
    data['b'] = (solution1, )
    solution2 = get_signals(data)['a']

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

