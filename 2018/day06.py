import os
from collections import Counter

script_dir = os.path.dirname(__file__)

data = []
input1 = 'input/day06.csv'

with open(os.path.join(script_dir, input1)) as f:
    for row in f:
        data.append(row)

def part1(polymer: list) -> int:
    return

def part2(polymer: list):
    return

if __name__ == "__main__":

    testdata = [
        '1, 1'
        '1, 6'
        '8, 3'
        '3, 4'
        '5, 5'
        '8, 9']

    assert part1(testdata) == 17