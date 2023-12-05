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
                retval[current_group] = retval[current_group] + [[range(values[1], values[1]+ values[2]), values[0]-values[1]]]

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
        if source in translation[0]:
            return source + translation[1]
    return source

def location_to_seed(source, data):
    translations = [
        'humidity-to-location',
        'temperature-to-humidity',
        'light-to-temperature',
        'water-to-light',
        'fertilizer-to-water',
        'soil-to-fertilizer',
        'seed-to-soil',
    ]
    for translation in translations:
        source = invtranslate(source, data[translation])
    return source

def invtranslate(source, data):
    for translation in data:
        if source - translation[1] in translation[0]:
            return source - translation[1]
    return source

def part1(data):
    """Solve part 1"""
    return min(map(lambda x: seed_to_location(x, data), data['seeds']))

def part2(data, stepsize = 100):
    """Solve part 2"""
    ranges = []
    for seed in range(0, len(data['seeds']), 2):
        ranges = ranges + [range(data['seeds'][seed], data['seeds'][seed] + data['seeds'][seed + 1])]
    
    location = 0
    step = stepsize
    while step >= 1:
        answer = -1
        while answer == -1:
            seed = location_to_seed(location, data)
            for range_check in ranges:
                if seed in range_check:
                    answer = location
                    break
            location = location + step
            if location % 1_000_000 == 0:
                print (location)
        location = answer - step
        step = int(step/stepsize)
    
    return answer

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = parse_lines(puzzle_input())
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
