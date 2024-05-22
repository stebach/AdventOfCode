"""
Solution for day 22 of year 2015
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    return dict([[y[0].replace(' ','').lower(), int(y[1])] for y in [x.strip().split(': ') for x in lines]])

def least_mana_used(data, my_hitpoint_start = 50, my_mana_start = 500, hard_mode = False):
    spells = {
        'magic_missle': [53, 4, 0, None, 0],
        'drain': [73, 2, 2, None, 0],
        'shield': [113, 0, 0, 'shield', 6],
        'poison': [173, 0, 0, 'poison', 6],
        'recharge': [229, 0, 0, 'recharge', 5],
    }
    state = (data['hitpoints'], data['damage'], my_hitpoint_start, my_mana_start, 0, 0, tuple({}.items()))
    queue = [state]

    best_cost = 5_000_000_000
    seen = set()

    while len(queue) > 0:
        current_state = queue.pop(0)
        if current_state[4] >= best_cost:
            continue

        enemy_hitpoints = current_state[0]
        my_hitpoints = current_state[2]
        my_turn = current_state[5] == 0

        if hard_mode and my_turn:
            my_hitpoints -= 1

        if enemy_hitpoints < 1:
            best_cost = current_state[4]
            continue
        if my_hitpoints < 1:
            continue

        active_effects = dict(current_state[6])
        my_armor = 0
        my_mana = current_state[3]


        for effect in active_effects.items():
            if effect[0] == 'shield':
                if active_effects[effect[0]] > 1:
                    my_armor = 7
            elif effect[0] == 'poison':
                enemy_hitpoints -= 3
            elif effect[0] == 'recharge':
                my_mana += 101
            else:
                print("UNKNOWN EFFECT: " + effect[0])
                exit()
            active_effects[effect[0]] -= 1
        
        active_effects = dict([x for x in active_effects.items() if x[1] > 0])

        if enemy_hitpoints < 1:
            best_cost = current_state[4]
            continue
        if my_hitpoints < 1:
            continue

        if my_turn:
            for spell in spells.items():
                if spell[1][3] != None and spell[1][3] in active_effects:
                    continue
                if spell[1][0] > my_mana:
                    continue
                
                new_effects = deepcopy(active_effects)
                if spell[1][3] != None:
                    new_effects[spell[1][3]] = spell[1][4]
                next_state = (enemy_hitpoints - spell[1][1], current_state[1], my_hitpoints + spell[1][2], my_mana - spell[1][0], current_state[4] + spell[1][0], (current_state[5] + 1) % 2, tuple(new_effects.items()))
                if next_state not in seen:
                    seen.add(next_state)
                    queue.append(next_state)
        else:
            next_state = (enemy_hitpoints, current_state[1], my_hitpoints + spell[1][2] - max(1, current_state[1] - my_armor), my_mana, current_state[4], (current_state[5] + 1) % 2, tuple(active_effects.items()))
            if next_state not in seen:
                seen.add(next_state)
                queue.append(next_state)

    return best_cost

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = least_mana_used(data)

    # Part 2
    solution2 = least_mana_used(data, hard_mode=True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

