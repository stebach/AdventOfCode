"""
Solution for day 09 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read()
    
def parse(data):
    result = {
        'score': 1,
        'total_score': 0,
        'garbage': [
        ],
        'garbageCount': 0,
        'groups': []
    }
    groups = [result]

    data = list(data[1:-1])
    currentGarbage = None
    currentGarbageCount = 0

    while len(data) > 0:
        nextChar = data.pop(0)
        if currentGarbage is not None:
            if nextChar == '>':
                groups[-1]['garbage'].append(currentGarbage)
                groups[-1]['garbageCount'] += currentGarbageCount
                currentGarbage = None
                currentGarbageCount = 0
            else:
                currentGarbageCount += 1
                currentGarbage += nextChar
                if nextChar == '!':
                    currentGarbageCount -= 1
                    currentGarbage += data.pop(0)
        elif nextChar == '<':
            currentGarbage = ''
        elif nextChar == '}':
            groups.pop()
        elif nextChar == '{':
            currentGroup = {
                'score': groups[-1]['score'] + 1,
                'total_score': 0,
                'garbage': [
                ],
                'garbageCount': 0,
                'groups': []
            }
            groups[-1]['groups'].append(currentGroup)
            groups.append(currentGroup)
        elif nextChar != ',':
            print("what to do whith: " + nextChar + "?")
            exit()

    calc_score(result)
    return result

def calc_score(result):
    result['total_score'] = result['score']
    for sub in result['groups']:
        calc_score(sub)
        result['total_score'] += sub['total_score']
        result['garbageCount'] += sub['garbageCount']

def parse_group(result, data):
    data = data[2:]
    print(data)

def get_score(data):
    return parse(data)['total_score']

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    parsed = parse(data)
    solution1 = parsed['total_score']

    # Part 2
    solution2 = parsed['garbageCount']

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
