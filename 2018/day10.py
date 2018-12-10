import os, re
from operator import add

script_dir = os.path.dirname(__file__)

data = []
testdata = []
input1 = 'input/day10.txt'
input_test = 'input/day10_test.txt'

def parserow(row):
    matches = re.search('position=<(.*), (.*)> velocity=<(.*), (.*)>', row)
    return (int(matches.group(1)), int(matches.group(2)), int(matches.group(3)), int(matches.group(4)))

with open(os.path.join(script_dir, input1)) as f:
    for line in f:
        data.append(parserow(line))

with open(os.path.join(script_dir, input_test)) as f:
    for line in f:
        testdata.append(parserow(line))  

def part1(coordinates: list) -> int:
    xcoordinates = list(zip(*coordinates))[0]
    ycoordinates = list(zip(*coordinates))[1]
    velocity_x = list(zip(*coordinates))[2]
    velocity_y = list(zip(*coordinates))[3]
    keeprunning = True
    second=0
    while keeprunning:
        spacecoordinates = list(zip(*[xcoordinates,ycoordinates]))
        xmin = min(xcoordinates)
        xmax = max(xcoordinates)
        ymin = min(ycoordinates)
        ymax = max(ycoordinates)

        print('running....')

        output_grid = []
        if ymax-ymin < 15: 
            for y in range(ymin, ymax+1):
                output = ''
                for x in range(xmin, xmax+1):
                    if (x,y) in spacecoordinates:
                        output += '#'
                    else:
                        output += '.'
                output_grid.append(output)
        else:
            second += 1
            xcoordinates = list(map(add, xcoordinates, velocity_x))
            ycoordinates = list(map(add, ycoordinates, velocity_y))  
            continue
        if output_grid:
            open('output/outputfile.txt', 'w').writelines(output+'\n' for output in output_grid)   
         

        text = input(f"Voer klaar in als je er klaar mee bent, al {second} seconden bezig: ")

        if text == "klaar":
            keeprunning = False
        else:
            second += 1
            xcoordinates = list(map(add, xcoordinates, velocity_x))
            ycoordinates = list(map(add, ycoordinates, velocity_y))      

def part2(coordinates: list, safe_distance: int) -> int:
    return

if __name__ == "__main__":

    #part1(testdata)

    part1(data)
