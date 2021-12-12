day = 12
example_input = f'day{day}example.txt'
problem_input = f'day{day}input.txt'

def solve(input, part1 = True):
    links = list(map(lambda x: x.strip().split('-'),open(input)))
    print(links)
    lookup = dict()
    for a,b in links:
        if a in lookup:
            lookup[a].append(b)
        else:
            lookup[a] = [b]
        if b in lookup:
            lookup[b].append(a)
        else:
            lookup[b] = [a]
    print(lookup)

    paths = navigate('start', [], set(['start']), lookup, part1)
    print(paths)
    print(len(paths))

from copy import deepcopy
def navigate(cur_loc : str, path : list, visited : set, lookup, twice):
    paths = []
    # print(f'{cur_loc = }, {visited = }')
    if cur_loc == 'end':
        path.append(cur_loc)
        return [path]

    for next in lookup[cur_loc]:
        if next != 'start' and (next not in visited or not twice):
            next_twice = True if next in visited else twice
            next_path = deepcopy(path)
            next_path.append(cur_loc)
            next_visted = deepcopy(visited)
            if cur_loc.islower():
                next_visted.add(cur_loc)
            paths += navigate(next, next_path, next_visted, lookup, next_twice)
    
    return paths
    
solve(example_input)
solve(problem_input)
solve(example_input, False)
solve(problem_input, False)