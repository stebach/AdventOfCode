"""
Solution for day 22 of year 2024
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: int(line.strip()), inputdata.readlines()))

def secret_number(data, times = 1):
    number = data
    for x in range(times):
        number = ((number * 64) ^ number) % 16777216
        number = ((number // 32) ^ number) % 16777216
        number = ((number * 2048) ^ number) % 16777216
    
    return number

def get_most_bananas_by_sequence(data):
    sequences = {}
    for starting_number in data:
        current_number = starting_number
        current_sequence = []
        seen = set()
        for x in range(2000):
            next_number = secret_number(current_number)
            current_sequence.append(next_number % 10 - current_number % 10)
            if len(current_sequence) > 4:
                current_sequence.pop(0)
            if len(current_sequence) == 4:
                current_sequence_tuple = tuple(current_sequence)
                if current_sequence_tuple not in seen:
                    seen.add(current_sequence_tuple)
                    if current_sequence_tuple not in sequences:
                        sequences[current_sequence_tuple] = next_number % 10
                    else:
                        sequences[current_sequence_tuple] += next_number % 10
            current_number = next_number
    return max(sequences.values())

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum([secret_number(x, 2000) for x in data])

    # Part 2
    solution2 = get_most_bananas_by_sequence(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

