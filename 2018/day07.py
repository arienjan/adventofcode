import os, csv, re

script_dir = os.path.dirname(__file__)

data = []
input1 = 'input/day07.csv'

with open(os.path.join(script_dir, input1)) as f:
    infile = csv.reader(f)
    for row in infile:
        matches = re.search('Step (.*) must (.*) step (.*) can', row[0])
        data.append([matches.group(1), matches.group(3)])

def recursive_add(steps, grid, used_nodes, unused_nodes, level):
    if not grid[level]:
        return grid
    else:
        grid.append([])
        for letter in grid[level]:
            ## zoek de mogelijke stappen
            possible_nodes = unused_nodes
            unused_nodes_ = []
            for step in steps:
                if letter in step[0]:
                    possible_nodes.append(step[1])
            
            for node in possible_nodes:
                add = True
                for step in steps:
                    if node == step[0]:
                        test_node = step[1]
                        for step2 in steps:
                            if step2[1] == test_node:
                                """
                                print('step2[0]', step2[0])
                                print('possible', possible_nodes)
                                print('used', used_nodes)
                                """
                                if step2[0] not in possible_nodes and step2[0] not in used_nodes:
                                    add = False
                                #print(add)
                if add:
                    used_nodes.add(node)   
                    grid[level+1].append(node)
                    print(grid)

                if not add:
                    unused_nodes_.append(node)
                #print(used_nodes)
            #print(possible_nodes)
        level += 1
        return recursive_add(steps, grid, used_nodes, unused_nodes_, level)

def part1(steps: list) -> int:
    ## find parents first
    zipped_list = list(zip(*steps))
    nodes = set()
    for item in zipped_list[0]:
        if item not in zipped_list[1]:
            nodes.add(item)

    grid = [[]]
    for i in nodes:
        grid[0].append(i)
    #print(grid[0])
    new_grid = recursive_add(steps, grid, nodes, [], 0)
    #print('outgrid', new_grid)
    outstring = ''
    for i in new_grid:
        for node in list(sorted(set(i))):
            outstring += node
    return outstring
"""

def recursive_add(steps, grid, level):
    if not grid[level]:
        return grid
    else:
        grid.append(set())
        for letter in grid[level]:
            for step in steps:
                if letter in step[1]:
                    grid[level+1].add(step[0])
        level += 1
        return recursive_add(steps, grid, level)

def recursive_order(grid, order, level):
    if not grid[level]:
        return order
    else:
        sub_letters = set()
        for i in range(level+1, len(grid)-1):
            for subletter in grid[i]:
                sub_letters.add(subletter)
        for letter in sorted(grid[level], reverse=True):
            print(letter, letter not in sub_letters)
            if letter not in sub_letters:
                order = letter + order
        level += 1
        return recursive_order(grid, order, level)

def part1(steps: list) -> int:
    ## find endings first
    zipped_list = list(zip(*steps))
    endings = []
    for item in zipped_list[1]:
        if item not in zipped_list[0]:
            endings.append(item)
    endings = set(endings)

    ## vind children en daarna moet je inde lijst checken of die children niet nog children hebben die voor de andere komen
    ## dus in het voorbeeld c heeft a en f, dat is prima
    ## maar daar onder zitten b, d en e, dus dan moet eerst gecheckt worden of b en d niet ook boven e vallen.
    ## en dat ook voor die children

    ##vind de parents en voeg alleen de parents doe dei ook uniek zijn en niet nog andere dezelfde children hebben
    grid = [set()]
    for i in endings:
        grid[0].add(i)
    new_grid = recursive_add(steps, grid, 0)

    ## bouw de string op recursief
    print(new_grid)
    order = ''
    final_order = recursive_order(new_grid, order, 0)
    print(final_order)
    return
"""
def part2(data):
    return

if __name__ == "__main__":

    testdata = [
        ['C', 'A'],
        ['C', 'F'],
        ['A', 'B'],
        ['A', 'D'],
        ['B', 'E'],
        ['D', 'E'],
        ['F', 'E']]


    print(data)

    assert part1(testdata) == 'CABDFE'
    
    print(part1(data))