"""
Solution for day 20 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([int(x) for x in line.strip().replace('p','').replace('a','').replace('v','').replace('=<','').replace('>','').split(',')])

def closest_long_term(data):
    smallest = 0
    smallest_idx = -1
    for x in range(len(data)):
        distance = abs(data[x][6]) + abs(data[x][7]) + abs(data[x][8])
        if smallest_idx == -1 or distance < smallest:
            smallest = distance
            smallest_idx = x
        elif distance == smallest:
            distance_check_1 = abs(data[smallest_idx][0] + data[smallest_idx][3] + data[smallest_idx][6]) + abs(data[smallest_idx][1] + data[smallest_idx][4] + data[smallest_idx][7]) + abs(data[smallest_idx][2] + data[smallest_idx][5] + data[smallest_idx][8])
            distance_check_2 = abs(data[x][0] + data[x][3] + data[x][6]) + abs(data[x][1] + data[x][4] + data[x][7]) + abs(data[x][2] + data[x][5] + data[x][8])
            if distance_check_2 < distance_check_1:
                smallest = distance
                smallest_idx = x
    return smallest_idx

def remove_collisions(data):
    particles = data
    for x in range(1_000):
        new_particles = []
        coords = set()
        remove = set()

        for particle in particles:
            new_particle = list(particle)
            new_particle[3] += new_particle[6]
            new_particle[4] += new_particle[7]
            new_particle[5] += new_particle[8]
            new_particle[0] += new_particle[3]
            new_particle[1] += new_particle[4]
            new_particle[2] += new_particle[5]

            key = str(new_particle[0]) + "_" + str(new_particle[1]) + "_" + str(new_particle[2])
            if key not in coords:
                coords.add(key)
            else:
                remove.add(key)

            new_particles.append(new_particle)

        if len(remove) > 0:
            new_particles = [y for y in new_particles if str(y[0]) + "_" + str(y[1]) + "_" + str(y[2]) not in remove]
        
        particles = new_particles
    return len(particles)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = closest_long_term(data)

    # Part 2
    solution2 = remove_collisions(data)

    print(solution2)
    exit()
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
