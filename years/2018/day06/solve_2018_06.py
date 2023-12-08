"""
Solution for day 06 of year 2018
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return list(map(int, line.strip().split(", ")))

def part1(data):
    """Solve part 1"""
    minX = min([x[0] for x in data])
    maxX = max([x[0] for x in data])
    minY = min([x[1] for x in data])
    maxY = max([x[1] for x in data])

    counts = {}
    infinite = []
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            minDistance = float('inf')
            minKey = -1;
            coord = [x, y]
            for i in range(0, len(data)):
                coord1 = data[i]
                distance = abs(coord[0] - coord1[0]) + abs(coord[1] - coord1[1])
                if distance < minDistance:
                    minDistance = distance
                    minKey = i
                elif distance == minDistance:
                    minKey = -1
            if minKey > -1:
                if not minKey in counts:
                    counts[minKey] = 0
                counts[minKey] = counts[minKey] + 1
                if x == minX or x == maxX or y == minY or y == maxY:
                    infinite = infinite + [minKey]

    return sorted([x for x in counts.items() if x[0] not in infinite], key=lambda x: x[1], reverse=True)[0][1]

def part2(data, maxDistance=10000):
    """Solve part 2"""
    minX = min([x[0] for x in data])
    maxX = max([x[0] for x in data])
    minY = min([x[1] for x in data])
    maxY = max([x[1] for x in data])

    area = 0

    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            totalDistance = 0
            coord = [x, y]
            for coord1 in data:
                totalDistance = totalDistance + abs(coord1[0] - coord[0]) + abs(coord1[1] - coord[1])
                if totalDistance > maxDistance:
                    break
            if totalDistance < maxDistance:
                area = area + 1

    return area

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
