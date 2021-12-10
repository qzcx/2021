example_input = 'day9example.txt'
problem_input = 'day9input.txt'


def parse():
    pass

def solve(input):
    heightmap = list(map(lambda x: list( map(int, list(x.strip() ) ) ), open(input)))
    global width, height
    width = len(heightmap[0])
    height = len(heightmap)
    #Pad with 9s
    heightmap.insert(0,[9]*width)
    heightmap.append([9]*width)
    for row in heightmap:
        row.append(9)
        row.insert(0,9)

    # print(heightmap)

    low_points = []
    s = 0
    for y in range(1,width+1):
        for x in range(1,height+1):
            cur = heightmap[x][y]
            if cur < heightmap[x+1][y] and \
                    cur < heightmap[x-1][y] and \
                    cur < heightmap[x][y+1] and \
                    cur < heightmap[x][y-1]:
                low_points.append((x,y))
                s += heightmap[x][y] + 1
    print(s)

    #Part 2
    basin_sizes = []
    visted = [[0] * len(heightmap[0]) for n in range(len(heightmap))]
    for p in low_points:
        size = explore(heightmap, visted, p)
        basin_sizes.append(size)
    
    basin_sizes.sort()
    
    print(f"{basin_sizes[-1] = } {basin_sizes[-2] = } {basin_sizes[-3] = }")
    print(f"{basin_sizes[-1] * basin_sizes[-2] *  basin_sizes[-3] = }")


def explore(heightmap, visted, cur_loc):
    #check if 9 or already visited
    if(heightmap[cur_loc[0]][cur_loc[1]] == 9 or visted[cur_loc[0]][cur_loc[1]] == 1):
        return 0

    #Set visted
    visted[cur_loc[0]][cur_loc[1]] = 1

    #permutate next locations
    next_locs = [(cur_loc[0]+1,cur_loc[1]),
                 (cur_loc[0]-1,cur_loc[1]),
                 (cur_loc[0],cur_loc[1]+1),
                 (cur_loc[0],cur_loc[1]-1)]
    #count this space
    s = 1
    #count neighbors
    for n in next_locs:
        s += explore(heightmap, visted, n)
    return s

solve(example_input)
solve(problem_input)

