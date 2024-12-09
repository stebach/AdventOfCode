"""
Solution for day 09 of year 2024
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read().strip()

def get_blocks(data):
    result = []
    id = 0
    for i in range(0, len(data), 2):
        result.append({
            'type': 'block',
            'id': id,
            'amount': int(data[i]),
        })
        id += 1
        if i + 1 < len(data) and int(data[i + 1]) > 0:
            result.append({
                'type': 'empty',
                'amount': int(data[i + 1]),
            })
        
    return result

def move_blocks(data):
    result = []
    localdata = deepcopy(data)
    totalempty = 0

    while len(localdata) > 0:
        if localdata[0]['type'] == 'block':
            result.append(localdata[0])
            localdata.pop(0)
        elif len(localdata) == 2:
            totalempty += localdata[0]['amount']
            result.append(localdata[1])
            localdata.pop(0)
            localdata.pop(0)
        else:
            empty = localdata[0]['amount']

            if localdata[-1]['amount'] <= empty:
                result.append({
                    'type': 'block',
                    'id': localdata[-1]['id'],
                    'amount': localdata[-1]['amount']
                })
                totalempty += localdata[-1]['amount']
                if localdata[-1]['amount'] < empty:
                    localdata[0]['amount'] -= localdata[-1]['amount']
                else:
                    localdata.pop(0)
                localdata.pop(-1)
                if len(localdata) > 0 and localdata[-1]['type'] == 'empty':
                    totalempty += localdata[-1]['amount']
                    localdata.pop(-1)
            else:
                result.append({
                    'type': 'block',
                    'id': localdata[-1]['id'],
                    'amount': empty
                })
                totalempty += empty
                localdata[-1]['amount'] -= empty
                localdata.pop(0)
    result.append({
        'type': 'empty',
        'amount': totalempty,
    })

    return result

def move_blocks_whole_files(data):
    result = []
    localdata = deepcopy(data)

    pos = len(localdata) - 1
    while pos > 0:
        if localdata[pos]['type'] == 'block':
            moved = False
            for pos2 in range(0, pos):
                if localdata[pos2]['type'] == 'empty' and localdata[pos2]['amount'] >= localdata[pos]['amount']:
                    moved = True
                    tmp = deepcopy(localdata[pos])
                    localdata[pos]['type'] = 'empty'
                    if 'id' in localdata[pos]:
                        del(localdata[pos]['id'])
                    localdata[pos2]['amount'] -= tmp['amount']
                    localdata.insert(pos2, tmp)
                    pos += 1

                    pos3 = pos2
                    while pos3 < len(localdata) - 1:
                        if localdata[pos3]['type'] == 'empty':
                            if localdata[pos3]['amount'] == 0:
                                localdata.pop(pos3)
                                pos -= 1
                            elif localdata[pos3+1]['type'] == 'empty':
                                localdata[pos3]['amount'] += localdata[pos3+1]['amount']
                                localdata.pop(pos3 + 1)
                                pos -= 1
                            else:
                                pos3 += 1
                        else:
                            pos3 += 1
                    break
            if not moved:
                pos -= 1
        else:
            pos -= 1

    return localdata

def checksum(data):
    localdata = deepcopy(data)
    result = 0
    pos = 0

    while len(localdata) > 0:
        if localdata[0]['type'] == 'block':
            result += pos * localdata[0]['id']
        localdata[0]['amount'] -= 1
        pos += 1
        if localdata[0]['amount'] == 0:
            localdata.pop(0)
    
    return result

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = checksum(move_blocks(get_blocks(data)))

    # Part 2
    solution2 = checksum(move_blocks_whole_files(get_blocks(data)))
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
