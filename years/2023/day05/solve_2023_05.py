"""
Solution for day 05 of year 2023
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def parse_lines(lines):
    retval = {}
    current_group = ''
    for line in lines:
        result = regex.search('seeds: ([0-9 ]+)', line)
        if result:
            retval['seeds'] = list(map(int, result.group(1).split( )))
        else:
            result = regex.search('([a-z]+-to-[a-z]+) map:', line)
            if (result):
                current_group = result.group(1)
                retval[current_group] = []
            elif line != "":
                values = list(map(int, line.split( )))
                retval[current_group] = retval[current_group] + [[[values[1], values[1] + values[2]], values[0]-values[1]]]

    return retval

def seed_to_location(source, data):
    translations = [
        'seed-to-soil',
        'soil-to-fertilizer',
        'fertilizer-to-water',
        'water-to-light',
        'light-to-temperature',
        'temperature-to-humidity',
        'humidity-to-location',
    ]
    for translation in translations:
        source = translate(source, data[translation])
    return source

def translate(source, data):
    for translation in data:
        if source >= translation[0][0] and source <= translation[0][1]:
            return source + translation[1]
    return source

def part1(data):
    """Solve part 1"""
    return min(map(lambda x: seed_to_location(x, data), data['seeds']))

def translateRange(seeds, data):
    retval = []
    while len(seeds) > 0:
        seed = seeds.pop()
        found = False
        minSeed = seed[0]
        maxSeed = seed[1]
        for translationRange in data:
            minRange = translationRange[0][0]
            maxRange = translationRange[0][1]
            diff = translationRange[1]
            if not (maxSeed < minRange or minSeed > maxRange):
                found = True
                if minSeed >= minRange:
                    if maxSeed <= maxRange:
                        retval = retval + [[minSeed + diff, maxSeed + diff]]
                    else:
                        retval = retval + [[minSeed + diff, maxRange + diff]]
                        seeds = seeds + [[maxRange + 1, maxSeed]]
                else:
                    if maxSeed <= maxRange:
                        retval = retval + [[minRange + diff, maxSeed + diff]]
                        seeds = seeds + [[minSeed, minRange - 1]]
                    else:
                        retval = retval + [[minRange + diff, maxRange + diff]]
                        seeds = seeds + [[minSeed, minRange - 1], [maxRange + 1, maxSeed]]
                break
        if not found:
            retval = retval + [seed]

    return retval

def part2(data, stepsize = 100):
    """Solve part 2"""
    seeds = [[data['seeds'][x], data['seeds'][x] + data['seeds'][x+1] - 1] for x in range(0, len(data['seeds']), 2)]
    translations = [
        'seed-to-soil',
        'soil-to-fertilizer',
        'fertilizer-to-water',
        'water-to-light',
        'light-to-temperature',
        'temperature-to-humidity',
        'humidity-to-location',
    ]
    for translation in translations:
        seeds = translateRange(seeds, data[translation])
    seeds = sorted(seeds, key=lambda x: x[0])
    return seeds[0][0]


def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = parse_lines(puzzle_input())
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
