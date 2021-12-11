#!/usr/bin/env python3
import fileinput
import pprint

octs = [list(map(int, line.strip())) for line in fileinput.input()]


def adjacent(y, x):
    locations = [(y - 1, x), (y - 1, x - 1), (y, x - 1), (y + 1, x - 1), (y + 1, x), (y + 1, x + 1), (y, x + 1),
                 (y - 1, x + 1)]
    return [(y1, x1) for y1, x1 in locations if 0 <= y1 < 10 and 0 <= x1 < 10 and octs[y1][x1] < 10]


def buildup(y,x, visited):
    if (y,x) in visited:
        return
    octs[y][x] += 1
    if octs[y][x] == 10:
        visited.add((y,x))
        for ny, nx in adjacent(y, x):
            buildup(ny, nx, visited)


def part1(steps):
    flashes = 0
    for _ in range(steps):
        for y in range(10):
            for x in range(10):
                flashed = set()
                buildup(y, x, flashed)
                flashes += len(flashed)

        for y in range(10):
            for x in range(10):
                if octs[y][x] >= 10:
                    octs[y][x] = 0

    pprint.pprint(octs)
    print(flashes)


def part2():
    steps = 0
    while True:
        steps += 1
        flashes = 0

        for y in range(10):
            for x in range(10):
                flashed = set()
                buildup(y, x, flashed)
                flashes += len(flashed)

        for y in range(10):
            for x in range(10):
                if octs[y][x] >= 10:
                    octs[y][x] = 0

        if flashes == 100:
            break

    pprint.pprint(octs)
    print(steps)


# part1(100)
part2()
