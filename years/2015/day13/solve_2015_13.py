"""
Solution for day 13 of year 2015
"""

import os
from queue import PriorityQueue
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {}
    for line in lines:
        (part1, person2) = line.strip().split(' happiness units by sitting next to ')
        check = part1.split(' would gain ')
        negative = 1
        if len(check) == 1:
            check = part1.split(' would lose ')
            negative = -1
        
        if check[0] not in result:
            result[check[0]] = {}
        result[check[0]][person2[0:-1]] = int(check[1]) * negative
    return result

def find_optimal_seating(data, add_me = False):
    queue = PriorityQueue()

    if add_me:
        data = deepcopy(data)
        for x in data:
            data[x]['__me__'] = 0
        data['__me__'] = dict([(x,0) for x in data])

    persons = [x for x in data]

    queue.put([persons[0]])
    
    max_change = 0
    while queue.qsize() > 0:
        check = queue.get()
        for person in persons:
            if person not in check:
                tmp = deepcopy(check)
                tmp.append(person)
                if len(tmp) == len(persons):
                    result = 0
                    for x in range(-1, len(persons) -1):
                        result += data[tmp[x]][tmp[x+1]] + data[tmp[x+1]][tmp[x]]
                    if result > max_change:
                        max_change = result
                else:
                    queue.put(tmp)
    return max_change

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_optimal_seating(data)

    # Part 2
    solution2 = find_optimal_seating(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
