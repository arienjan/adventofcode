import os, csv
from itertools import cycle

script_dir = os.path.dirname(__file__)

data = []
input1 = 'input/day01.csv'

with open(os.path.join(script_dir, input1)) as f:
    infile = csv.reader(f)
    for row in infile:
        data.append(int(row[0]))

def part1(array):
    return sum(array)

def part2(array):
    i, frequency= 0, 0
    seen_freqs = {0}
    for change in cycle(array):
        i+=1
        frequency += change
        if frequency in seen_freqs:
            return frequency
        else:
            seen_freqs.add(frequency)

if __name__ == "__main__":

    assert part1([+1, +1, +1]) == 3
    assert part1([+1, +1, -2]) == 0
    assert part1([-1, -2, -3]) == -6

    print(part1(data))

    assert part2([+1, -1]) == 0
    assert part2([+3, +3, +4, -2, -4]) == 10
    assert part2([-6, +3, +8, +5, -6]) == 5
    assert part2([+7, +7, -2, -7, -4]) == 14

    print(part2(data))