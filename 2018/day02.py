import os, csv
from collections import Counter

script_dir = os.path.dirname(__file__)

data = []
input1 = 'input/day02.csv'

with open(os.path.join(script_dir, input1)) as f:
    infile = csv.reader(f)
    for row in infile:
        data.append(row[0])

def part1(array):
    id2, id3 = 0, 0
    for boxId in array:
        counts = Counter(boxId).values()
        for count in set(counts):
            if count == 2: id2 += 1
            if count == 3: id3 += 1
    return id2 * id3


def part2(array):
    for boxId1 in array:
        for boxId2 in array:
            diff = 0
            outputId = ''
            for i in range(len(boxId1)):
                if boxId1[i] != boxId2[i]: 
                    diff += 1
                    outputId = boxId1[:i] + boxId1[i+1:] 
                if diff > 1:
                    break
            if diff == 1: return outputId

if __name__ == "__main__":

    assert part1(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']) == 12

    print(part1(data))

    assert part2(['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']) == 'fgij'

    print(part2(data))