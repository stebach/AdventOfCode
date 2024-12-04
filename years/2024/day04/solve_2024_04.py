"""
Solution for day 04 of year 2024
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple(list(line.strip()))


def search_word(data, word):
    word_as_list = list(word)
    word_count = 0
    directions = [(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]

    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col].lower() == word_as_list[0].lower():
                for direction in directions:
                    tmp = [(row, col)]
                    for i in range(1, len(word_as_list)):
                        tmp.append((row + direction[1] * i, col + direction[0] * i))
                        if row + direction[1] * i >= len(data) or row + direction[1] * i < 0 or col + direction[0] * i >= len(data[row]) or col + direction[0] * i < 0 or data[row + direction[1] * i][col + direction[0] * i].lower() != word_as_list[i].lower():
                            break
                        elif i == len(word_as_list) - 1:
                            word_count += 1

    return word_count

def search_crossed_3letter_word(data, word):
    word_as_list = list(word.lower())
    middle_char = word_as_list[1]
    outer_chars = (word_as_list[0], word_as_list[2])
    word_count = 0


    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col].lower() == middle_char:
                if row + 1 >= len(data) or row - 1 < 0 or col + 1 >= len(data[row]) or col - 1 < 0:
                    continue
                if data[row + 1][col + 1].lower() in outer_chars \
                   and data[row - 1][col - 1].lower() in outer_chars \
                   and (
                       data[row + 1][col + 1].lower() != data[row - 1][col - 1].lower() \
                        or outer_chars[0] == outer_chars[1]
                   ) \
                   and data[row + 1][col - 1].lower() in outer_chars \
                   and data[row - 1][col + 1].lower() in outer_chars \
                   and (
                       data[row + 1][col - 1].lower() != data[row - 1][col + 1].lower() \
                        or outer_chars[0] == outer_chars[1]
                   ):
                    word_count += 1

    return word_count

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = search_word(data, 'xmas')

    # Part 2
    solution2 = search_crossed_3letter_word(data, 'mas')
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
