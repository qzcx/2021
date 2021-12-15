day = 15
example_input = f'day{day}example.txt'
problem_input = f'day{day}input.txt'

import numpy as np
from heapq import *

def loc_mapping(loc, row_width):
    return loc[0] * row_width + loc[1]

def solve(input, part2=False):
    risk_map = np.array(list(map(lambda x: list(map(int,(list(x.strip())))),open(input)) ))

    if part2:
        for y in range(5):
            for x in range(5):
                if x == 0:
                    row_map = np.array((risk_map+x+y)%10 + ((risk_map+x+y)/10).astype(int))
                else:
                    row_map = np.concatenate((row_map,np.array((risk_map+x+y)%10) +  ((risk_map+x+y)/10).astype(int)),axis=1)
            if y == 0:
                new_map = row_map
            else:
                new_map = np.concatenate((new_map,row_map),axis=0)
        risk_map = new_map

    #dijkstra's path finding :)
    paths_priority = []
    row_width = risk_map.shape[1]
    loc_cost = {loc_mapping((0,0), row_width): 0}
    heappush(paths_priority,(0, (0,0), [] ) ) #cost, cur, path
    while(len(paths_priority) > 0):
        cost, cur, path = heappop(paths_priority)
        if(cur == (risk_map.shape[0]-1, row_width-1)):
            # path
            print(path)
            print(cost)
            break

        next_locs =  [(y,cur[1]) for y in range(cur[0]-1, cur[0]+2,2)]
        next_locs += [(cur[0],x) for x in range(cur[1]-1, cur[1]+2,2)]
        next_locs = list(filter(lambda next: next[1] < row_width and next[1] >= 0 and
                                    next[0] < risk_map.shape[0] and next[0] >= 0 and 
                                    (next[0],next[1]) not in path, next_locs) )

        for next in next_locs:
            next_path = path.copy()
            next_path.append(next)
            next_cost = cost+risk_map[next[0]][next[1]]
            next_loc_pos = loc_mapping(next, row_width)
            if next_loc_pos not in loc_cost or next_cost < loc_cost[next_loc_pos]:
                loc_cost[next_loc_pos] = next_cost
                heappush(paths_priority,(next_cost, next, next_path ) )


# solve(example_input)
# solve(problem_input)

# solve(example_input, part2=True)
solve(problem_input, part2=True)