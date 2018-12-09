import os
from collections import Counter

script_dir = os.path.dirname(__file__)

data = []
input1 = 'input/day05.txt'

with open(os.path.join(script_dir, input1)) as f:
    invalue=f.read().replace('\n', '')
    for i in invalue:
        data.append(i)

def part1(polymer: list) -> int:
    i=0
    while i < len(polymer)-1:
        value = polymer[i]
        nextvalue = polymer[i+1]

        if ((value.isupper() and not nextvalue.isupper()) or (not value.isupper() and nextvalue.isupper())) and (value.lower() == nextvalue.lower()):
            del polymer[i+1]
            del polymer[i]
            i -= 1
        else:
            i += 1
    return len(polymer)

def part2(polymer: list):
    values = {''}
    value, minvalue = 0, 10**10
    for key in Counter(polymer).keys():
        values.add(key.lower())
    values.remove('')
    for unit in values:
        testpolymer = list(filter(lambda x: x!=unit and x!=unit.upper(), polymer))
        value = part1(testpolymer)
        if value < minvalue:
            minvalue = value
    return minvalue

if __name__ == "__main__":

    teststring = 'dabAcCaCBAcCcaDA'
    testdata = []
    for i in teststring:
        testdata.append(i)

    part1_testdata = testdata[:]
    assert part1(part1_testdata) == 10

    part1_data = data[:]
    print(part1(data))

    part2_testdata = testdata[:]
    assert part2(part2_testdata) == 4

    part2_data = data[:]
    print(part2(data))
