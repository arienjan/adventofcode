import os, csv, re

script_dir = os.path.dirname(__file__)

data = []
input1 = 'input/day03.csv'

with open(os.path.join(script_dir, input1)) as f:
    for row in f:
        data.append(row)

def get_claim_data(claim: str):
    matches = re.search('@ (\d+),(\d+): (\d+)x(\d+)', claim)
    return [int(matches.group(1)), int(matches.group(2)), int(matches.group(3)), int(matches.group(4))]

# def create_entire_patch(claims: list):
#     xmax, ymax = 0, 0
#     for claim in claims:
#         claim_data = get_claim_data(claim)
#         xmax = max(xmax, claim_data[0] + claim_data[2])
#         ymax = max(ymax, claim_data[1] + claim_data[3])
#     entire_patch = [[0 for x in range(xmax)] for y in range(ymax)]
#     return entire_patch

def part1(claims: list) ->  int:
    patches, overlapping = {tuple()}, {tuple()}
    for claim in claims:
        claim_data = get_claim_data(claim)
        for x in range(claim_data[0], claim_data[0] + claim_data[2]):
            for y in range(claim_data[1], claim_data[1] + claim_data[3]):
                coordinate = tuple([x,y])
                if coordinate in patches:
                    overlapping.add(coordinate)
                patches.add(coordinate)
    return len(overlapping)-1

def part2(claims: list):
    patches = {tuple()}
    for claim in claims:
        claim_data = get_claim_data(claim)
        for x in range(claim_data[0], claim_data[0] + claim_data[2]):
            for y in range(claim_data[1], claim_data[1] + claim_data[3]):
                patches.add(tuple([x,y])

    return len(overlapping)-1

if __name__ == "__main__":
    
    assert part1([
        '#1 @ 1,3: 4x4', 
        '#2 @ 3,1: 4x4', 
        '#3 @ 5,5: 2x2']) == 4

    print(part1(data))