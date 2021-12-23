day = 20
example_input = f'day{day}example.txt'
problem_input = f'day{day}input.txt'

#100x100 -> 102x102 -> 104x104
#Convert input into 1s and 0s
#Algorithm process
    #Single pass over pixels
        #Track sliding window
            #contains three lines of the grid
        #Generate new grid with each 3x3 set of values

def swap_to_num(s):
    return s.replace('#','1').replace('.','0')

def swap_to_hash(s):
    return s.replace('1','#').replace('0','.')

import numpy as np
def solve(input, count=2):
    with open(input) as f:
        lines = f.readlines()
        lookup = list(lines[0].strip() )
    initial_grid = np.array([  list(line.strip() ) 
                        for line in lines[2:]])
    print(lookup)
    print("Initial Grid")
    print(initial_grid.shape)
    print(f'{initial_grid}')
    grid = initial_grid
    init = '.' 
    for i in range(count):
        grid = ie_algo(grid, lookup, init)
        init = lookup[0] if init == '.' else lookup[-1]
        # print(f"Next init {init}")
    np.savetxt(f"day20_output{i}.txt",grid, fmt='%s', delimiter='')
    print(np.count_nonzero(grid == '#'))

def ie_algo(grid, lookup, init='.'):
    shape = grid.shape
    pad_grid = np.full( (shape[0]+4,shape[1]+4), init, dtype=str )

    # print(pad_grid)
    pad_grid[2:-2,2:-2] = grid
    grid = pad_grid
    new_grid = np.full( (shape[0]+2,shape[1]+2),'.', dtype=str)
    # print("Padded Grid")
    # print(pad_grid)
    for y in range(shape[0]+2):
        for x in range(shape[1]+2):
             binary_string = "".join( list(map(str, list(pad_grid[y:y+3,x:x+3].flatten()) ))  )
            #  print(f'{y=} {x=} : {binary_string}')
             new_grid[y,x] = lookup[int(swap_to_num(binary_string),2)]
    # print("New Grid")
    print(new_grid.shape)
    # print(new_grid)
    return new_grid


# solve(example_input)
# solve(problem_input)


# solve(example_input,50)
solve(problem_input,50)