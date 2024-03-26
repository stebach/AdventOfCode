"""
Solution for day 04 of year 2021
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    numbers = list(map(int, lines.pop(0).split(",")))
    boards = []
    current_board = []
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            current_board = []
            boards.append(current_board)
        else:
            current_board.append([int(x) for x in line.split(" ") if len(x) > 0])
    return (
        numbers,
        boards
    )

def play_until_win(data):

    winners = []
    number = 0
    while len(winners) == 0:
        number = data[0].pop(0)
        for pos, card in enumerate(data[1]):
            card = [[num if num != number else -1 for num in row ] for row in card]
            sums = [sum(row) for row in card]
            data[1][pos] = card
            if -5 in sums:
                winners.append(card)
            else:
                sums = [sum([row[x] for row in card]) for x in range(5)]
                if -5 in sums:
                    winners.append(card)
    for winner in winners:
        data[1].remove(winner)
    return sum([sum([col for col in row if col > 0]) for row in winners[0]]) * number

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = play_until_win(data)

    # Part 2
    solution2 = 0
    while len(data[1]) > 0:
        solution2 = play_until_win(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

