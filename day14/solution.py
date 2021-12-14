#!/usr/bin/env python3
import collections
import fileinput
import itertools

template = None
rules = {}

for line in fileinput.input():
    line = line.strip()
    if template is None:
        template = line
        continue
    elif len(line):
        pair, element = line.split(" -> ")
        rules[pair] = element


def expand(template):
    while True:
        polymer = []
        for a,b in itertools.pairwise(template):
            polymer.append(a)
            polymer.append(rules[a+b])
        polymer.append(b)
        yield ''.join(polymer)


def part1(polymer):
    for _ in range(10):
        polymer = next(expand(polymer))
    elements = collections.Counter(polymer).most_common()
    return elements[0][1] - elements[-1][1]


print(part1(template))
