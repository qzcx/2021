
example_input = 'day5example.txt'
problem_input = 'day5input.txt'

#

def parse(input_line):
    splits = input_line.strip().split(' -> ')
    lines = tuple(tuple(map(int,split.split(','))) for split in splits)
    return lines

def solve(input, grid_size=10, no_diag=True):
    lines = list( map (parse, open(input)))
    vents = [ [0 for n in range(grid_size)] 
                for n in range(grid_size)]

    # print(lines)
    # print_vents(vents)

    for line in lines:
        mark_vents(vents, line, no_diag)
    
    # print_vents(vents)
    print(f'{count_overlap(vents) = }')

def mark_vents(vents, line, no_diag=True):
    x1,y1 = line[0]
    x2,y2 = line[1]
    if no_diag and not ((x1 == x2) ^ (y1 == y2)):
        return

    while(x1 != x2 or y1 != y2):
        vents[x1][y1] += 1
        if(x1 != x2):
            x1 = x1+1 if x2 > x1 else x1-1
        if(y1 != y2):
            y1 = y1+1 if y2 > y1 else y1-1
        assert(x1 >= 0 and y1 >= 0)
    vents[x2][y2] += 1

def count_overlap(vents):
    count = 0
    for row in vents:
        for vent in row:
            count += 1 if vent > 1 else 0
    return count

def print_vents(vents):
    print("Printing vents:")
    for row in vents:
        print(row)
    print("End of vent print")

solve(example_input)
solve(problem_input, grid_size=1000)


solve(example_input, no_diag=False)
solve(problem_input, grid_size=1000, no_diag=False)





