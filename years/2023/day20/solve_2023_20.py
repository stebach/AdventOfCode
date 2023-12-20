"""
Solution for day 20 of year 2023
"""

import os
import copy
from collections import deque
from math import floor, gcd
from functools import reduce

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(tuple(map(lambda line: line.strip(), inputdata.readlines())))

def parse_lines(lines):
    result = {}
    targets = { }
    for line in lines:
        parts = line.split(' -> ')
        type = None
        if parts[0][0] in '%&':
            type = parts[0][0]
        name = parts[0][1:] if type is not None else parts[0]
        config = {}
        if type == '%':
            config = { 'global': False }
        result[name] = (type, tuple(parts[1].split(', ')), config)
        for target in parts[1].split(', '):
            if not target in targets:
                targets[target] = []
            targets[target].append(name)
    for name, targetlist in targets.items():
        for target in targetlist:
            if not name in result:
                result[name] = (None, tuple(), { 'global': True })
            if (result[name][0] == '&'):
                result[name][2][target] = False
    return result

def push_button(data):
    signals = deque()
    signals.append(('broadcaster', False, 'button'))

    signalCount = [0,0]

    while len(signals) > 0:
        signal = signals.popleft()
        signalCount[0 if signal[1] else 1] += 1
        module = data[signal[0]]

        if module[0] == None: # broadcaster
            module[2]['global'] = signal[1]
            for target in module[1]:
                signals.append((target, signal[1], signal[0]))
        elif module[0] == '%':
            if not signal[1]:
                module[2]['global'] = not module[2]['global']
                for target in module[1]:
                    signals.append((target, module[2]['global'], signal[0]))
        elif module[0] == '&':
            module[2][signal[2]] = 1 if signal[1] else 0
            to_send = sum(module[2].values()) != len(module[2].values())
            for target in module[1]:
                signals.append((target, to_send, signal[0]))
    
    return (signalCount, data)


def part1(data):
    """Solve part 1"""
    runs = 0
    todo = 1000
    orig = copy.deepcopy(data)
    wrk = copy.deepcopy(data)
    total_count = (0,0)
    while runs < todo:
        runs += 1
        signal_count, wrk = push_button(wrk)
        total_count = (total_count[0] + signal_count[0], total_count[1] + signal_count[1])
        if orig == wrk:
            total_count = (total_count[0] * floor(todo / runs), total_count[1] * floor(todo / runs))
            runs = todo - (todo % runs)
    return (total_count[0] * total_count[1])

def lcm(a, b):
    return int(abs(a * b) / gcd(a, b))


def get_groups(data, target):
    check = [name for name in data if target in data[name][1]]
    if (len(check) == 1 and data[check[0]][0] == '&'):
        return get_groups(data, check[0])
    else:
        if len([data[x][0] for x in data if x in check and data[x][0] != '&']) == 0:
            return [get_groups(data, x) for x in check]
        else:
            return check;

def get_runs(groups, data):
    mode = 0
    for x in range(len(groups)):
        if (type(groups[x]) is list):
            groups[x] = get_runs(groups[x], data)
        else:
            mode = 1
            cp = copy.deepcopy(data)
            tmp = 0
            while not cp[groups[x]][2]['global']:
                tmp += 1
                push_button(cp)
            groups[x] = tmp
    if mode == 1:
        result = 0
        for x in groups:
            result |= x
        return result
    return reduce(lcm, groups)

def part2(data):
    """Solve part 2"""
    groups = get_groups(data, 'rx')
    return get_runs(groups, data)

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
