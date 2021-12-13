#!/usr/bin/env python3
import fileinput

instructions = []
points = set()

for line in fileinput.input():
    line = line.strip()
    if line.startswith('fold'):
        axis, position = line.replace("fold along ", "").split("=")
        instructions.append((axis, int(position)))
    elif len(line):
        x, y = line.split(",")
        points.add((int(x), int(y)))

for axis, position in instructions:
    if axis == 'y':
        points = set([(x, y - 2 * max(0, y - position)) for x, y in points])
    else:
        points = set([(x - 2 * max(0, x - position), y) for x, y in points])
    # print(len(points))


def show():
    mx = max(points)[0]
    my = sorted(points, key=lambda p: p[1], reverse=True)[0][1]
    grid = [[' ' for _ in range(mx + 1)] for _ in range(my + 1)]
    for x, y in points:
        grid[y][x] = '#'
    for y in range(my + 1):
        for x in range(mx + 1):
            print(grid[y][x], end='')
        print()


show()
