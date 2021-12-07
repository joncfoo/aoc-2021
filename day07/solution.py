#!/usr/bin/env python3
import collections
import fileinput
import sys

positions = collections.Counter(int(n) for line in fileinput.input()
                                for n in line.split(','))
for n in range(max(positions.keys())):
    if n not in positions:
        positions[n] = 0


def part1():
    min_fuel = sys.maxsize
    best_position = -1

    for current_position in positions.keys():
        fuel = sum(abs(other_position - current_position) * positions[other_position]
                   for other_position in positions.keys())
        if fuel < min_fuel:
            min_fuel = fuel
            best_position = current_position

    return best_position, min_fuel


def part2():
    min_fuel = sys.maxsize
    position = -1

    for current_position in positions.keys():
        fuel = 0
        for other_position in positions.keys():
            distance = abs(other_position - current_position)
            #  sum of consecutive numbers
            fuel += int((distance / 2) * (1 + distance)) * positions[other_position]
        if fuel < min_fuel:
            min_fuel = fuel
            position = current_position

    return position, min_fuel


print(part1())
print(part2())
