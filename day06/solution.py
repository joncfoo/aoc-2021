#!/usr/bin/env python3
import fileinput

ns = [int(n) for line in fileinput.input() for n in line.split(',')]


def smort(days):
    fish_timers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for n in ns:
        fish_timers[n] += 1

    for day in range(days):
        repro_fish = fish_timers[0]
        fish_timers = fish_timers[1:]
        fish_timers[6] += repro_fish
        fish_timers.append(repro_fish)
    return sum(fish_timers)


def not_smort(fishes, days):
    for day in range(days):
        for n in range(len(fishes)):
            if fishes[n] == 0:
                fishes[n] = 6
                fishes.append(8)
            else:
                fishes[n] -= 1
        print(day, len(fishes))
    return len(fishes)


# print(not_smort(256))
print(smort(256))
