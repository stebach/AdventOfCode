"""
Solution for day 21 of year 2020
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()
    parts = line[:-1].split(" (contains ")
    return (tuple(parts[0].split(" ")), tuple(parts[1].split(", ")))

def find_harmless_ingredients(data):
    alergens = get_alergens(data)

    alergen_list = sum([alergens[x] for x in alergens], [])
    harmless = []
    for food in data:
        for ingredient in food[0]:
            if ingredient not in alergen_list:
                harmless.append(ingredient)
    return harmless

def get_alergens(data):
    alergens = {}
    for food in data:
        for alergen in food[1]:
            if alergen not in alergens:
                alergens[alergen] = list(food[0])
            else:
                alergens[alergen] = list(set(alergens[alergen]).intersection(list(food[0])))
    return alergens

def get_ordered_allergen_ingredients(data):
    alergens = get_alergens(data)
    fixed = [alergens[x][0] for x in alergens if len(alergens[x]) == 1]
    done = False
    max = 10
    while not done:
        done = True
        for alergen in alergens:
            if len(alergens[alergen]) > 1:
                alergens[alergen] = [x for x in alergens[alergen] if x not in fixed]
                if len(alergens[alergen]) == 1:
                    fixed.append(alergens[alergen][0])
                else:
                    done = False
    alergen_list = [x for x in alergens]
    alergen_list.sort()
    ordered_ingredients = [alergens[x][0] for x in alergen_list]
    return ",".join(ordered_ingredients)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = len(find_harmless_ingredients(data))

    # Part 2
    solution2 = get_ordered_allergen_ingredients(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
