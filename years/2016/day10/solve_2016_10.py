"""
Solution for day 10 of year 2016
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = []
    for line in lines:
        line = line.strip().split(' ')
        if line[0] == 'value':
            while len(result) <= int(line[-1]):
                result.append({'has':[], 'gives':[]})
            result[int(line[-1])]['has'].append(int(line[1]))
        else:
            while len(result) <= int(line[1]):
                result.append({'has':[], 'gives':[]})
            result[int(line[1])]['gives'].append([line[5], int(line[6])])
            result[int(line[1])]['gives'].append([line[10], int(line[11])])
    
    return tuple(result)

def find_responsible(data, comparison = None):
    data = deepcopy(data)
    done = False
    outputs = []
    while not done:
        done = True
        for botnr, bot in enumerate(data):
            if len(bot['has']) == 2:
                done = False
                if (bot['has'][0],bot['has'][1]) == comparison or (bot['has'][1],bot['has'][0]) == comparison:
                    return botnr
                if bot['gives'][0][0] == 'bot':
                    data[bot['gives'][0][1]]['has'].append(min(bot['has']))
                else:
                    while len(outputs) <= bot['gives'][0][1]:
                        outputs.append([])
                    outputs[bot['gives'][0][1]].append(min(bot['has']))
                if bot['gives'][1][0] == 'bot':
                    data[bot['gives'][1][1]]['has'].append(max(bot['has']))
                else:
                    while len(outputs) <= bot['gives'][1][1]:
                        outputs.append([])
                    outputs[bot['gives'][1][1]].append(max(bot['has']))
                bot['has'].clear()
    return outputs

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_responsible(data, (61,17))

    # Part 2
    tmp = find_responsible(data)
    solution2 = tmp[0][0] * tmp[1][0] * tmp[2][0]
    print(solution2)
    exit()
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
