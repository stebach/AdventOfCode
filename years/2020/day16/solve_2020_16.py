"""
Solution for day 16 of year 2020
"""

import os
import regex
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    mode = 0
    fields = {}
    my_ticket = None
    other_tickets = []
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            mode += 1
            continue
        elif line in ('your ticket:','nearby tickets:'):
            continue
        if mode == 0:
            res = regex.findall('^([^:]*): ([0-9]+)\-([0-9]+) or ([0-9]+)\-([0-9]+)$',line)
            fields[res[0][0]] = ((int(res[0][1]),int(res[0][2])),(int(res[0][3]),int(res[0][4])))
        elif mode == 1:
            my_ticket = tuple(map(int, line.split(',')))
        elif mode == 2:
            other_tickets.append(tuple(map(int, line.split(','))))
    return (
        fields,
        my_ticket,
        tuple(other_tickets)
    )

def check1(data):
    invalid = []
    for ticket in data[2]:
        for number in ticket:
            found = False
            for type in data[0]:
                for typerange in data[0][type]:
                    if number >= typerange[0] and number <= typerange[1]:
                        found = True
                        break
            if not found:
                invalid.append(number)
    return sum(invalid)

def get_departure_value(data):
    valid_tickets = []
    for ticket in data[2]:
        ticket_valid = True
        for number in ticket:
            found = False
            for type in data[0]:
                for typerange in data[0][type]:
                    if number >= typerange[0] and number <= typerange[1]:
                        found = True
                        break
            if not found:
                ticket_valid = False
                break
        if ticket_valid:
            valid_tickets.append(ticket)
    valid_tickets.append(data[1])
    
    matches = dict([[x, [y for y in range(0, 20)]] for x in data[0]])


    while sum([len(matches[x]) for x in matches]) > len(matches):
        for x in matches:
            if len(matches[x]) > 1:
                matches_copy = deepcopy(matches[x])
                for ticket in valid_tickets:
                    for m in matches_copy:
                        if (ticket[m] < data[0][x][0][0] or ticket[m] > data[0][x][0][1]) and (ticket[m] < data[0][x][1][0] or ticket[m] > data[0][x][1][1]):
                            matches[x].remove(m)
        for x in matches:
            if len(matches[x]) == 1:
                for y in matches:
                    if y != x and matches[x][0] in matches[y]:
                        matches[y].remove(matches[x][0])

    res = 1
    for x in matches:
        if x.startswith('departure'):
            res *= data[1][matches[x][0]]

    return res


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = check1(data)

    # Part 2
    solution2 = get_departure_value(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
