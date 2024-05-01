"""
Solution for day 24 of year 2022
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {
        'blizzards':[],
        'bounds': (len(lines[0].strip()) - 1, len(lines) - 1),
        'start': (1, 0),
        'to_start': (1, 1),
        'to_end': (len(lines[0].strip()) - 2, len(lines) - 2),
        'end': (len(lines[0].strip()) - 2, len(lines) - 1)
    }
    for (y, line) in enumerate(lines):
        for (x, char) in enumerate(line.strip()):
            if char == '<':
                result['blizzards'].append(([x,y], (-1,0)))
            elif char == '>':
                result['blizzards'].append(([x,y], (1,0)))
            elif char == '^':
                result['blizzards'].append(([x,y], (0,-1)))
            elif char == 'v':
                result['blizzards'].append(([x,y], (0,1)))

    result['blizzards'] = tuple(result['blizzards'])
    return result

def get_minutes(data, there_and_back_again = False):
    blizzards = deepcopy(data['blizzards'])
    states = [(data['start'][0], data['start'][1])]
    minutes = 0

    moves = ((0,0),(0,1),(0,-1),(1,0),(-1,0))

    goals = [[data['to_end'], data['end']]]
    if there_and_back_again:
        goals.append(
            [data['to_start'], data['start']]
        )
        goals.append(
            [data['to_end'], data['end']]
        )

    while True:
        minutes += 1
        new_states = []


        blizzards = move_blizzards(blizzards, data)
        blizz_pos = dict([tuple(x[0]), x[1]] for x in blizzards)

        for state in states:
            for move in moves:
                new_pos = (state[0] + move[0], state[1] + move[1])
                if new_pos not in blizz_pos and new_pos not in new_states and ((new_pos[0] > 0 and new_pos[1] > 0 and new_pos[0] < data['bounds'][0] and new_pos[1] < data['bounds'][1]) or (new_pos in (data['start'], data['end']))):
                    new_states.append(new_pos)

        states = new_states

        if goals[0][0] in states:
            states = [goals.pop(0)[1]]
            minutes += 1
            if len(goals) == 0:
                return minutes
            blizzards = move_blizzards(blizzards, data)


def move_blizzards(blizzards, data):
    blizzards = tuple(([x[0][0] + x[1][0], x[0][1] + x[1][1]], x[1]) for x in blizzards)
    blizzards = tuple(([1 if x[0][0] == data['bounds'][0] else x[0][0], 1 if x[0][1] == data['bounds'][1] else x[0][1]], x[1]) for x in blizzards)
    blizzards = tuple(([data['bounds'][0] - 1 if x[0][0] == 0 else x[0][0], data['bounds'][1] - 1 if x[0][1] == 0 else x[0][1]], x[1]) for x in blizzards)
    return blizzards
        

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_minutes(data)

    # Part 2
    solution2 = get_minutes(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
