"""
Solution for day 21 of year 2015
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    return dict([[y[0].replace(' ','').lower(), int(y[1])] for y in [x.strip().split(': ') for x in lines]])

def fight(me, boss):
    result = [me['hitpoints'], boss['hitpoints']]
    fighters = [me, boss]
    fighter = 0
    while len([x for x in result if x < 1]) == 0:
        result[(fighter + 1) % 2] -= max(1, fighters[fighter]['damage'] - fighters[(fighter + 1) % 2]['armor'])
        fighter = (fighter + 1) % 2
    return result

def get_cheapest(boss, most_expensive = False):
    weapons = {
        'Dagger': {
            'cost': 8,
            'damage': 4,
            'armor': 0
        },
        'Shortsword': {
            'cost': 10,
            'damage': 5,
            'armor': 0
        },
        'Warhammer': {
            'cost': 25,
            'damage': 6,
            'armor': 0
        },
        'Longsword': {
            'cost': 40,
            'damage': 7,
            'armor': 0
        },
        'Greataxe': {
            'cost': 74,
            'damage': 8,
            'armor': 0
        },
    }
    armors = {
        'None': {
            'cost': 0,
            'damage': 0,
            'armor': 0
        },
        'Leather': {
            'cost': 13,
            'damage': 0,
            'armor': 1
        },
        'Chainmail': {
            'cost': 31,
            'damage': 0,
            'armor': 2
        },
        'Splintmail': {
            'cost': 53,
            'damage': 0,
            'armor': 3
        },
        'Bandedmail': {
            'cost': 75,
            'damage': 0,
            'armor': 4
        },
        'Platemail': {
            'cost': 102,
            'damage': 0,
            'armor': 5
        },
    }
    rings = {
        'None': {
            'cost': 0,
            'damage': 0,
            'armor': 0
        },
        'Damage +1': {
            'cost': 25,
            'damage': 1,
            'armor': 0
        },
        'Damage +2': {
            'cost': 50,
            'damage': 2,
            'armor': 0
        },
        'Damage +3': {
            'cost': 100,
            'damage': 3,
            'armor': 0
        },
        'Defense +1': {
            'cost': 20,
            'damage': 0,
            'armor': 1
        },
        'Defense +2': {
            'cost': 40,
            'damage': 0,
            'armor': 2
        },
        'Defense +3': {
            'cost': 80,
            'damage': 0,
            'armor': 3
        },
    }

    best_cost = 5_000_000
    if most_expensive:
        best_cost = 0
    for weapon in weapons.items():
        for armor in armors.items():
            for ring1 in rings.items():
                for ring2 in rings.items():
                    if ring2[0] != 'None' and ring2[0] == ring1[0]:
                        continue
                    cost = sum([x[1]['cost'] for x in [weapon, armor, ring1, ring2]])
                    if (not most_expensive and cost >= best_cost) or (most_expensive and cost <= best_cost):
                        continue
                    damage_val = sum([x[1]['damage'] for x in [weapon, armor, ring1, ring2]])
                    armor_val = sum([x[1]['armor'] for x in [weapon, armor, ring1, ring2]])
                    me = {
                        'hitpoints': 100,
                        'damage': damage_val,
                        'armor': armor_val
                    }
                    fightdata = fight(me, boss)
                    if not most_expensive and fightdata[0] > 0:
                        best_cost = cost
                    elif most_expensive and fightdata[0] < 1:
                        best_cost = cost
    return best_cost


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_cheapest(data)

    # Part 2
    solution2 = get_cheapest(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
