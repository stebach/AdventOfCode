"""
Solution for day 22 of year 2019
"""

import os
from copy import deepcopy
from math import floor

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()
    if line[0:20] == 'deal with increment ':
        return ('increment', int(line[20:]))
    if line[0:4] == 'cut ':
        return ('cut', int(line[4:]))
    return ('deal',)



def find_position(number_of_cards, card, iterations, orders, reverse = False):
    orders = reduce_orders(deepcopy(orders), number_of_cards)

    total_interations = 0
    final_orders = []
    current = 1
    while total_interations != iterations:
        if iterations & current:
            total_interations = total_interations | current
            final_orders = final_orders + orders
        current *= 2
        orders = reduce_orders(orders + orders, number_of_cards)

    orders = reduce_orders(final_orders, number_of_cards)

    if reverse:
        orders = orders[::-1]

    for order in orders:
        if order[0] == 'increment':
            if reverse:
                mod_inverse = pow(order[1],-1,number_of_cards)
                card = (card * mod_inverse) % number_of_cards
            else:
                card = (card * order[1]) % number_of_cards
        elif order[0] == 'deal':
            card = number_of_cards - card - 1
        elif order[0] == 'cut':
            size = order[1] % number_of_cards
            if reverse:
                card = (card + size) % number_of_cards
            else:
                if size < card:
                    card = card - size
                else:
                    card = (card + number_of_cards - size) % number_of_cards
        else:
            print(order[0])
            exit()

    return card

def reduce_orders(new_orders, number_of_cards):
    new_orders = list(new_orders)
    while len(new_orders) > 3:
        i = len(new_orders) - 2
        while i >= 0:
            if len(new_orders) -1 > i:
                order1 = new_orders[i]
                order2 = new_orders[i+1]
                if order1[0] == 'deal':
                    if order2[0] == 'deal':
                        del new_orders[i]
                        del new_orders[i]
                    elif order2[0] == 'cut':
                        new_orders[i] = ('cut', number_of_cards - order2[1])
                        new_orders[i+1] = order1
                    elif order2[0] == 'increment':
                        new_orders[i:i+2] = [
                            order2,
                            ('cut', number_of_cards + 1 - order2[1]),
                            order1
                        ]
                elif order1[0] == 'cut':
                    if order2[0] == 'cut':
                        new_orders[i] = ('cut', (order1[1] + order2[1]) % number_of_cards)
                        del new_orders[i+1]
                    elif order2[0] == 'increment':
                        tmp = ('cut', (order1[1] * order2[1]) % number_of_cards)
                        new_orders[i] = order2
                        new_orders[i+1] = tmp
                elif order1[0] == 'increment':
                    if order2[0] == 'increment':
                        new_orders[i] = ('increment', (order1[1] * order2[1]) % number_of_cards)
                        del new_orders[i+1]
                else:
                    print("ERROR 2")
                    exit()
            i -= 1
    return new_orders

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1

    solution1 = find_position(10007, 2019, 1, data)

    # Part 2
    shuffles = 101741582076661
    solution2 = find_position(119315717514047, 2020, shuffles, data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
