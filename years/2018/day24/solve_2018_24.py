"""
Solution for day 24 of year 2018
"""

import os
import regex
from queue import PriorityQueue
from math import floor
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = [[],[]]
    index = 0
    for line in lines:
        line = line.strip()
        if line == 'Infection:':
            index = 1
        elif line not in ("Immune System:", ""):
            match = regex.findall(r'^([0-9]+) units each with ([0-9]+) hit points (\([^\)]+\) )?with an attack that does ([0-9]+) ([^ ]+) damage at initiative ([0-9]+)$', line)
            if len(match) == 0:
                print("ERR")
                print(line)
                exit()
            weakness = None
            immunity = None
            if len(match[0][2]) > 0:
                checks = match[0][2][1:-2].split('; ')
                for check in checks:
                    if check[0:8] == 'weak to ':
                        weakness = tuple(check[8:].split(', '))
                    elif check[0:10] == 'immune to ':
                        immunity = tuple(check[10:].split(', '))
                    else:
                        print (check[0:10])
                        exit()
            result[index].append([int(match[0][0]) * int(match[0][3]), int(match[0][5]), match[0][4], int(match[0][0]), int(match[0][3]), int(match[0][1]), weakness, immunity ])
    return result

def set_targets(attacking, attacking_index, defending, defending_index, targeting):
    attacking_queue = PriorityQueue()
    targets = set()

    for x in attacking:
        if x[3] == 0:
            continue
        attacking_queue.put((-x[0], -x[1], x))

    while attacking_queue.qsize() > 0:
        attacking_check = attacking_queue.get()
        defending_queue = PriorityQueue()
        for x in defending:
            if x[3] == 0:
                continue
            if tuple(x) not in targets:
                damage = attacking_check[2][0]
                if x[6] != None and attacking_check[2][2] in x[6]:
                    damage *= 2
                if x[7] != None and attacking_check[2][2] in x[7]:
                    damage = 0
                if damage > 0:
                    defending_queue.put((-damage,-x[0], -x[1],x))
        if defending_queue.qsize() > 0:
            final_target = defending_queue.get()[3]
            targets.add(tuple(final_target))
            targeting.put((-attacking_check[2][1], attacking_index, attacking.index(attacking_check[2]), defending_index, defending.index(final_target)))

def fight(data):
    targeting = PriorityQueue()
    set_targets(data[0], 0, data[1], 1, targeting)
    set_targets(data[1], 1, data[0], 0, targeting)

    while targeting.qsize() > 0:
        tmp = targeting.get()
        damage = data[tmp[1]][tmp[2]][0]
        if data[tmp[3]][tmp[4]][6] != None and data[tmp[1]][tmp[2]][2] in data[tmp[3]][tmp[4]][6]:
            damage *= 2
        killcount = floor(damage / data[tmp[3]][tmp[4]][5])
        data[tmp[3]][tmp[4]][3] = max(data[tmp[3]][tmp[4]][3] - killcount, 0)
        data[tmp[3]][tmp[4]][0] = data[tmp[3]][tmp[4]][3] * data[tmp[3]][tmp[4]][4]


def part1(data):
    """Solve part 1"""
    data2 = deepcopy(data)
    while True:
        fight(data2)
        check1 = [x[3] for x in data2[0] if x[3] > 0]
        check2 = [x[3] for x in data2[1] if x[3] > 0]
        if len(check1) == 0:
            return sum(check2)
        if len(check2) == 0:
            return sum(check1)

def part2(data):
    """Solve part 2"""
    step = 10000
    boost = 0
    while True:
        boost += step
        data2 = deepcopy(data)
        last = (0,0)
        for x in range(len(data2[0])):
            data2[0][x][4] += boost
            data2[0][x][0] = data2[0][x][4] * data2[0][x][3]
        while True:
            fight(data2)
            check1 = [x[3] for x in data2[0] if x[3] > 0]
            check2 = [x[3] for x in data2[1] if x[3] > 0]
            check = (sum(check1), sum(check2))
            if len(check1) == 0 or check == last:
                break
            if len(check2) == 0:
                if step == 1:
                    return sum(check1)
                boost -= step
                step = int(step/10)
                break
            last = check


def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
