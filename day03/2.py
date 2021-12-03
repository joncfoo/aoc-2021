#!/usr/bin/env python3
import fileinput, itertools

def process(ns, i, high):
    ns.sort()

    if len(ns) == 1:
        return ns[0]

    p = {k: list(g) for k, g in itertools.groupby(ns, lambda x: x[i])}

    if len(p['1']) >= len(p['0']):
        return process(p['1' if high else '0'], i+1, high)
    else:
        return process(p['0' if high else '1'], i+1, high)

numbers = [line.strip() for line in fileinput.input()]

oxygen = process(numbers, 0, True)
co2 = process(numbers, 0, False)

print(oxygen, co2)
print(int(oxygen, 2) * int(co2, 2))
