import os, csv, re
from itertools import izip_longest

script_dir = os.path.dirname(__file__)

data = []
input1 = 'input/day03.csv'

with open(os.path.join(script_dir, input1)) as f:
    for row in f:
        data.append(row)

def get_claim_data(claim: str):
    matches = re.search('@ (\d+),(\d+): (\d+)x(\d+)', claim)
    return [matches.group(1), matches.group(2), matches.group(3), matches.group(4)]

def create_entire_patch(claims: list):
    xmax, ymax = 0, 0
    for claim in claims:
        claim_data = get_claim_data(claim)
        xmax = max(xmax, claim_data[0] + claim_data[2])
        ymax = max(ymax, claim_data[1] + claim_data[3])
    entire_patch = [[0 for x in range(xmax)] for y in range(ymax)]


def part1(claims: list) ->  int:
    #entire_patch = create_entire_patch(claims)
    for claim in claims:
        claim_data = get_claim_data(claim)

def part2(array):
    return 'hoi'

if __name__ == "__main__":
    
    part1(data)