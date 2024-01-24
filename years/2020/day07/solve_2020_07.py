"""
Solution for day 07 of year 2020
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return dict(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().split(' bags contain ')
    rules = line[1].replace(' bag, ',' bags.').replace(' bags, ', ' bags.').replace(' bag.', ' bags.').split(' bags.')[:-1]
    if rules[0] == 'no other':
        return (line[0], tuple())
    rules = tuple([tuple([y[1], int(y[0])]) for y in [x.split(' ',1) for x in rules]])
    return (line[0],rules)

def count_bags(bags, to_count):
    result = 1
    for bag in bags[to_count]:
        result += count_bags(bags, bag[0]) * bag[1]
    return result

def contains_bag(bags, haystack, needle):
    found = False
    for bag in bags[haystack]:
        found = found or bag[0] == needle or contains_bag(bags, bag[0], needle)
    return found

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum([contains_bag(data, x, 'shiny gold') for x in data])

    # Part 2
    solution2 = count_bags(data, 'shiny gold') - 1

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
