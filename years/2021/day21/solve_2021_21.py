"""
Solution for day 21 of year 2021
"""

import os
from copy import deepcopy
from collections import deque

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return int(line.strip().split(': ')[1])

def play_deterministic(data):
    positions = [data[0] - 1, data[1] - 1]
    scores = [0, 0]
    current_player = 0
    next_roll = 0
    rolls = 0
    while len([x for x in scores if x > 999]) == 0:
        positions[current_player] = (positions[current_player] + (next_roll) % 100 + (next_roll + 1) % 100 + (next_roll + 2) % 100 + 3) % 10
        scores[current_player] += positions[current_player] + 1
        next_roll = (next_roll + 3) % 100
        current_player = (current_player + 1) % 2
        rolls += 3
    return [x for x in scores if x < 1000][0] * rolls

def play_dirac(data):
    datamap = {}
    throws = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1
    }
    queue = deque([
        {
            'positions': [data[0] - 1, data[1] - 1],
            'scores': [0, 0],
            'current_player': 0, 
            'count': 1
        }
    ])
    wins = [0,0]
    while len(queue) > 0:
        next_game_orig = queue.pop()
        fromkey = "_".join([str(x) for x in [*next_game_orig['positions'],*next_game_orig['scores'],next_game_orig['current_player']]])
        if fromkey in datamap:
            add_winners(datamap, fromkey, wins, next_game_orig['count'])
        else:
            datamap[fromkey] = []
            for roll in throws:
                next_game = deepcopy(next_game_orig)
                current_player = next_game['current_player']
                next_game['positions'][current_player] = (next_game['positions'][current_player] + roll) % 10
                next_game['scores'][current_player] += next_game['positions'][current_player] + 1
                next_game['current_player'] = (next_game['current_player'] + 1) % 2 
                tokey = "_".join([str(x) for x in [*next_game['positions'],*next_game['scores'],next_game['current_player']]])
                next_game['count'] *= throws[roll]
                if next_game['scores'][current_player] > 20:
                    datamap[fromkey].append(['win_' + str(current_player), throws[roll]])
                    wins[current_player] += next_game['count']
                else:
                    datamap[fromkey].append([tokey, throws[roll]])
                    queue.append(next_game)
    return max(wins)

def add_winners(datamap, fromkey, wins, amount):
    for (target, multiplicator) in datamap[fromkey]:
        if target == 'win_0':
            fromkey = None
            wins[0] += amount * multiplicator
        elif target == 'win_1':
            fromkey = None
            wins[1] += amount * multiplicator
        else:
            add_winners(datamap, target, wins, amount * multiplicator)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = play_deterministic(data)

    # Part 2
    solution2 = play_dirac(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
