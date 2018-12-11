import operator

def calculate_area(x: int, y:int, serial_number: int, size = 3) -> int:
    x_range = list(x for x in range(x,x+size))
    y_range = list(y for y in range(y,y+size))
    for x in x_range:
        for y in y_range:
            rack_id = x+10
            power_level = (((((rack_id*y)+serial_number)*rack_id) // 100)%10)-5
            yield  power_level
    return

def part1(serial_number: int) -> int:
    output = {}
    for x in range(1, 300-1):
        for y in range(1, 300-1):
            output[str(x)+','+str(y)]=sum(list(calculate_area(x, y, serial_number)))
    return max(output.items(), key=operator.itemgetter(1))[0]

def part2(serial_number: int) -> int:
    output = {}
    for size in range(1, 300-1):
        for x in range(1, 300+2-size):
            for y in range(1, 300+2-size):
                output[str(x)+','+str(y)+','+str(size)]=sum(list(calculate_area(x, y, serial_number, size)))
    return max(output.items(), key=operator.itemgetter(1))[0]
        
    return

if __name__ == "__main__":

    assert part1(18) == '33,45'
    assert part1(42) == '21,61'

    print(part1(6392))

    assert part2(18) == '90,269,16'
    assert part2(42) == '232,251,12'

    print(part2(6392))
