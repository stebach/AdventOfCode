"""
Solution for day 15 of year 2015
"""

import os
import regex
from queue import SimpleQueue

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return dict(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = regex.findall(r'^([a-z]+): capacity ([-0-9]+), durability ([-0-9]+), flavor ([-0-9]+), texture ([-0-9]+), calories ([-0-9]+)$', line.strip(), regex.IGNORECASE)
    return (line[0][0], {
        'capacity': int(line[0][1]),
        'durability': int(line[0][2]),
        'flavor': int(line[0][3]),
        'texture': int(line[0][4]),
        'calories': int(line[0][5])
    })


def get_high_score(data, limit=None):
    ingredients = [x for x in data]
    amounts = [1] * len(ingredients)
    seen = set()


    queue = SimpleQueue()
    queue.put(tuple(amounts))

    max_score = 0

    while queue.qsize() > 0:
        entry = queue.get()
        if sum(entry) == 100:
            if limit is not None:
                calories = sum([data[x[1]]['calories'] * entry[x[0]] for x in enumerate(data)])
                if calories != limit:
                    continue
            score = get_score(data, ingredients, entry)
            if score > max_score:
                max_score = score
        else:
            for pos in range(len(entry)):
                next_entry = tuple([x[1] + (1 if x[0] == pos else 0) for x in enumerate(entry)])
                if next_entry not in seen:
                    seen.add(next_entry)
                    if limit is not None:
                        calories = sum([data[x[1]]['calories'] * next_entry[x[0]] for x in enumerate(data)])
                        if calories > limit:
                            continue
                    queue.put(next_entry)

    return max_score

def get_score(data, ingredients, amounts):
    capacity = max(0, sum([data[x[1]]['capacity'] * amounts[x[0]] for x in enumerate(data)]))
    durability = max(0, sum([data[x[1]]['durability'] * amounts[x[0]] for x in enumerate(data)]))
    flavor = max(0, sum([data[x[1]]['flavor'] * amounts[x[0]] for x in enumerate(data)]))
    texture = max(0, sum([data[x[1]]['texture'] * amounts[x[0]] for x in enumerate(data)]))

    return capacity * durability * flavor * texture

def solve(data):
    # Part 1
    solution1 = get_high_score(data)

    # Part 2
    solution2 = get_high_score(data, 500)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
