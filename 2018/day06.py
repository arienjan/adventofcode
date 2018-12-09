import os, operator
from collections import Counter

script_dir = os.path.dirname(__file__)

data = []
input1 = 'input/day06.csv'

with open(os.path.join(script_dir, input1)) as f:
    for row in f:
        newrow = row.replace(' ', '')
        newrow = newrow.replace(u'\n', '')
        newrow = newrow.split(',')
        data.append([int(newrow[0]), int(newrow[1])])

def part1(coordinates: list) -> int:
    xmax = max(list(zip(*coordinates))[0])
    ymax = max(list(zip(*coordinates))[1])

    #geef de coordinaten een nummer om uit te lezen
    coordinate_dict={}
    for i in range(len(coordinates)):
        coordinate_dict[i]=coordinates[i]

    grid = [[0 for y in range(ymax+1)] for x in range(xmax+1)]
    ## voor elk punt in dit grid berekenen welk coordinaat het dichtse bij is
    for x, ylist in enumerate(grid):
        for y, value in enumerate(ylist):
            min_distance = 10**10
            for key, value in coordinate_dict.items():
                distance = abs(x-value[0]) + abs(y-value[1])
                if distance == min_distance:
                    grid[x][y] = '.'
                if distance < min_distance:
                    min_distance = distance
                    grid[x][y] = key
    
    ## count the elements in the edge rows, to ignore these
    edges = {'.'}

    for y in grid[0]: edges.add(y)
    for y in grid[len(grid)-1]: edges.add(y)
    for x in list(zip(*grid))[0]: edges.add(x)
    for x in list(zip(*grid))[len(list(zip(*grid)))-1]: edges.add(x)

    ## count the elements in the list, not in edges
    counts = Counter([x for sublist in grid for x in sublist])

    for count in list(counts):
        if count in edges:
            del counts[count]
    #print(counts)
    return counts.most_common(1)[0][1]

def part2(coordinates: list, safe_distance: int) -> int:
    xmax = max(list(zip(*coordinates))[0])
    ymax = max(list(zip(*coordinates))[1])

    #geef de coordinaten een nummer om uit te lezen
    coordinate_dict={}
    for i in range(len(coordinates)):
        coordinate_dict[i]=coordinates[i]

    grid = [[0 for y in range(ymax+1)] for x in range(xmax+1)]
    ## voor elk punt in dit grid berekenen welk coordinaat het dichtse bij is
    safe_locations = 0
    for x, ylist in enumerate(grid):
        for y, value in enumerate(ylist):
            distance_sum = 0
            for key, value in coordinate_dict.items():
                distance_sum += abs(x-value[0]) + abs(y-value[1])

            if distance_sum<safe_distance:
                safe_locations += 1
    return safe_locations

if __name__ == "__main__":

    testdata = [
        [1, 1],
        [1, 6],
        [8, 3],
        [3, 4],
        [5, 5],
        [8, 9]]

    assert part1(testdata) == 17

    print(part1(data)) 

    assert part2(testdata, 32) == 16

    print(part2(data, 10000))