#!/usr/bin/env python3
import fileinput
import math
import queue
import statistics

close_rule = {')': '(', ']': '[', '}': '{', '>': '<'}
syntax_error_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
open_rule = {'(': ')', '[': ']', '{': '}', '<': '>', }
incomplete_error_points = {')': 1, ']': 2, '}': 3, '>': 4}


def part1(line):
    q = queue.LifoQueue()
    for c in line:
        if c in '([{<':
            q.put(c)
        elif close_rule[c] == q.get():
            continue
        else:
            # invalid
            return syntax_error_points[c]


def part2(line):
    q = queue.LifoQueue()
    for c in line:
        if c in '([{<':
            q.put(c)
        elif close_rule[c] == q.get():
            continue
        else:
            # invalid
            return
    points = 0
    while not q.empty():
        points = points * 5 + incomplete_error_points[open_rule[q.get()]]
    return points


# part 1
print(sum(filter(None, (part1(line.strip()) for line in fileinput.input()))))

# part 2
# print(statistics.median(filter(None, (part2(line.strip()) for line in fileinput.input()))))
