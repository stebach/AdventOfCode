"""
Solution for day 21 of year 2022
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {}
    for line in lines:
        parts = line.strip().split(': ')
        parts2 = parts[1].split(' ')
        if len(parts2) > 1:
            result[parts[0]] = {
                'type': parts2[1],
                'attr': [parts2[0], parts2[2]]
            }
        else:
            result[parts[0]] = {
                'type': 'num',
                'attr': int(parts[1])
            }

    return result

def get_monkey_roll(data):
    return get_monkey_call(data, 'root')

def get_monkey_call(data, name):
    if data[name]['type'] == 'num':
        return data[name]['attr']
    elif data[name]['type'] == '+':
        return get_monkey_call(data, data[name]['attr'][0]) + get_monkey_call(data, data[name]['attr'][1])
    elif data[name]['type'] == '-':
        return get_monkey_call(data, data[name]['attr'][0]) - get_monkey_call(data, data[name]['attr'][1])
    elif data[name]['type'] == '/':
        return int(get_monkey_call(data, data[name]['attr'][0]) / get_monkey_call(data, data[name]['attr'][1]))
    elif data[name]['type'] == '*':
        return get_monkey_call(data, data[name]['attr'][0]) * get_monkey_call(data, data[name]['attr'][1])
    else:
        print(data[name]['type'])
        exit()

def get_number_to_pass_equality_test(data):
    val11 = get_monkey_call(data, data['root']['attr'][0])
    val12 = get_monkey_call(data, data['root']['attr'][1])

    data['humn']['attr'] += 10
    val21 = get_monkey_call(data, data['root']['attr'][0])
    val22 = get_monkey_call(data, data['root']['attr'][1])
    key_to_test = data['root']['attr'][0]
    value_to_get = val22
    direction = 1
    if abs(val11 - val12) < abs(val21 - val22):
        direction = -1
    if val21 == val22:
        if abs(val12 - val11) < abs(val22 - val21):
            direction = -1
        key_to_test = data['root']['attr'][1]
        value_to_get = val12

    while get_monkey_call(data, key_to_test) != value_to_get:
        diff = abs(get_monkey_call(data, key_to_test) - value_to_get)
        multiplicator = 1
        if diff > 10_000_000_000:
            multiplicator = 100_000_000
        elif diff > 100_000_000:
            multiplicator = 1_000_000
        elif diff > 1_000_000:
            multiplicator = 10_000
        elif diff > 10_000:
            multiplicator = 100
        data['humn']['attr'] += direction * multiplicator

    return data['humn']['attr']

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_monkey_roll(data)

    # Part 2
    solution2 = get_number_to_pass_equality_test(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
