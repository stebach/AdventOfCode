"""
Solution for day 09 of year 2015
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
        (locations, distance) = line.strip().split(' = ')
        locations = locations.split(' to ')
        if locations[0] not in result:
            result[locations[0]] = {}
        result[locations[0]][locations[1]] = int(distance)
        if locations[1] not in result:
            result[locations[1]] = {}
        result[locations[1]][locations[0]] = int(distance)
    return result

def find_shortest(data, longest = False):
    queue = PriorityQueue()
    cities = [x for x in data]

    for city in cities:
        for city2 in data[city]:
            queue.put((data[city][city2], [city, city2]))
    
    min_distance = sum([sum([data[x][y] for y in data[x]]) for x in data])
    if longest:
        min_distance = 0
    while queue.qsize() > 0:
        check = queue.get()
        for city in cities:
            if city not in check[1]:
                tmp = (check[0] + data[check[1][-1]][city], deepcopy(check[1]))
                tmp[1].append(city)
                if len(tmp[1]) == len(cities):
                    if (not longest and tmp[0] < min_distance) or (longest and tmp[0] > min_distance):
                        min_distance = tmp[0]
                else:
                    if (not longest and tmp[0] < min_distance) or (longest):
                        queue.put(tmp)
    return min_distance

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_shortest(data)

    # Part 2
    solution2 = find_shortest(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
