"""
Solution for day 13 of year 2018
"""

import os
from queue import PriorityQueue
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(tuple(map(lambda line: line.rstrip(), inputdata.readlines())))

def parse_lines(lines):
    new_lines = []
    carts = []
    for y, line in enumerate(lines):
        new_line = '';
        for x, char in enumerate(line):
            if char in '/-\\|+ ':
                new_line += char
            elif char == '>':
                new_line += '-'
                carts.append([y,(x,y),(1,0),0])
            elif char == '<':
                new_line += '-'
                carts.append([y,(x,y),(-1,0),0])
            elif char == '^':
                new_line += '|'
                carts.append([y,(x,y),(0,-1),0])
            elif char == 'v':
                new_line += '|'
                carts.append([y,(x,y),(0,1),0])
        new_lines.append(new_line)
    return [
        tuple(new_lines),
        carts
    ]

def part1(data):
    """Solve part 1"""
    carts = deepcopy(data[1])
    while True:
        new_carts = []
        queue = PriorityQueue()
        for cart in carts:
            queue.put(cart)
        while not queue.empty():
            cart = queue.get()
            if len(new_carts) > 0:
                if cart[1] in [x[1] for x in new_carts]:
                    return cart[1]

            cart[1] = (cart[1][0] + cart[2][0], cart[1][1] + cart[2][1])
            cart[0] = cart[1][1]

            rail = data[0][cart[1][1]][cart[1][0]]
            if rail == '+':
                if cart[3] % 3 == 0:
                    cart[2] = (cart[2][1], -cart[2][0])
                elif cart[3] % 3 == 2:
                    cart[2] = (-cart[2][1], cart[2][0])
                cart[3] += 1
            elif rail == '\\':
                cart[2] = (cart[2][1], cart[2][0])
            elif rail == '/':
                cart[2] = (-cart[2][1], -cart[2][0])
            elif rail not in '-|':
                print("UNKNOWN RAIL: " + rail)
                exit()

            if len(new_carts) > 0:
                if cart[1] in [x[1] for x in new_carts]:
                    return cart[1]

            new_carts.append(cart)
        carts = new_carts


def part2(data):
    """Solve part 2"""
    carts = deepcopy(data[1])
    while True:
        new_carts = []
        queue = PriorityQueue()
        for cart in carts:
            queue.put(cart)
        while not queue.empty():
            cart = queue.get()
            if len(new_carts) > 0:
                if cart[1] in [x[1] for x in new_carts]:
                    new_carts = [x for x in new_carts if x[1] != cart[1]]
                    continue

            cart[1] = (cart[1][0] + cart[2][0], cart[1][1] + cart[2][1])
            cart[0] = cart[1][1]

            rail = data[0][cart[1][1]][cart[1][0]]
            if rail == '+':
                if cart[3] % 3 == 0:
                    cart[2] = (cart[2][1], -cart[2][0])
                elif cart[3] % 3 == 2:
                    cart[2] = (-cart[2][1], cart[2][0])
                cart[3] += 1
            elif rail == '\\':
                cart[2] = (cart[2][1], cart[2][0])
            elif rail == '/':
                cart[2] = (-cart[2][1], -cart[2][0])
            elif rail not in '-|':
                print("UNKNOWN RAIL: " + rail)
                exit()

            if len(new_carts) > 0:
                if cart[1] in [x[1] for x in new_carts]:
                    new_carts = [x for x in new_carts if x[1] != cart[1]]
                    continue

            new_carts.append(cart)
        carts = new_carts
        if len(carts) == 1:
            return carts[0][1]

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
