"""
Solution for day 16 of year 2022
"""

import os
import regex
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {}
    for line in lines:
        line = regex.findall(r'^Valve ([a-z]{2}) has flow rate=([0-9]+); tunnels? leads? to valves? ([a-z ,]+)$', line.strip(), regex.IGNORECASE)

        result[line[0][0]] = (int(line[0][1]), tuple(line[0][2].split(', ')))
    return result

def release_preassure(data, time):
    cache = {}
    max_release = calc_max_possible(data, "AA", [], time, cache)
    return max_release

def release_preassure2(data, time):
    queue = set([('AA',tuple([]),0)])
    nonzero_valves = [x for x in data if data[x][0] > 0]
    for i in range(time):
        new_queue = set([])
        for state in queue:
            if len(state[1]) == len(nonzero_valves):
                new_queue.add(state)
                continue
            if state[0] in nonzero_valves and state[0] not in state[1]:
                new_open = list(state[1])
                new_open.append(state[0])
                new_queue.add((state[0], tuple(sorted(new_open)), state[2] + (time-i-1) * data[state[0]][0]))
            for connection in data[state[0]][1]:
                new_queue.add((connection, state[1], state[2]))
        queue = new_queue

    queue = list(queue)
    clean_queue = {}
    for item in queue:
        if item[1] not in clean_queue or clean_queue[item[1]] < item[2]:
            clean_queue[item[1]] = item[2]

    clean_queue_keys = [x for x in clean_queue]
    result = 0
    for me in range(0, len(clean_queue_keys) -1):
        for elephant in range(me + 1, len(clean_queue_keys)):
            valid = True
            for valve in clean_queue_keys[me]:
                if valve in clean_queue_keys[elephant]:
                    valid = False
                    break
            if valid:
                result = max(result, clean_queue[clean_queue_keys[me]] + clean_queue[clean_queue_keys[elephant]])

    return result


def calc_max_possible(data, position, open, timeleft, cache):
    if timeleft < 1:
        return 0
    key = position + "-" + "|".join(sorted(open)) + "-" + str(timeleft)
    if key not in cache:
        currentPos = data[position]
        max_release = 0
        release = (timeleft - 1) * currentPos[0]
        new_open = deepcopy(open)
        new_open.append(position)
        for connection in currentPos[1]:
            if release > 0 and position not in open:
                max_release = max(max_release, release + calc_max_possible(data, connection, new_open, timeleft-2, cache))
            max_release = max(max_release, calc_max_possible(data, connection, open, timeleft-1, cache))
        cache[key] = max_release
    return cache[key]

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = release_preassure(data, 30)

    # Part 2
    solution2 = release_preassure2(data, 26)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
