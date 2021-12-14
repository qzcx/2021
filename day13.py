day = 13
example_input = f'day{day}example.txt'
problem_input = f'day{day}input.txt'

import numpy as np

def solve(input, part1=True):
    points = list(map(lambda x: list(x.strip().split(',')), open(input) ) )
    fold_lines = list(filter(lambda x: len(x) == 1 and x[0] != '', points))

    np_points = np.array( list( map( lambda x: list(map(int,x)), #Convert to int
                            filter(lambda x: len(x) == 2, points) ) ) ) #Filter each list to just the points
    
    print(np_points)
    xmax, ymax = np_points.max(axis=0)
    print(f"{xmax = } {ymax = }")
    paper = np.zeros([ymax+1, xmax+1])
    for x, y in np_points:
        paper[y][x] = 1
    print(paper)

    if part1:
        fold_lines = fold_lines[:1]

    for fold in fold_lines:
        fold_text = fold[0].split(' ')[2]
        dim, pos = fold_text.split('=')
        pos = int(pos)
        print(f'{dim = } {pos = }')
        if dim == 'y':
            for y in range(pos):
                for x in range(xmax+1):
                    paper[y][x] = 1 if paper[ymax - y][x] else paper[y][x]
            ymax = pos - 1
            old_paper = paper.copy()
            paper = old_paper[:ymax+1]
        elif dim == 'x':
            for x in range(pos):
                for y in range(ymax+1):
                    paper[y][x] = 1 if paper[y][xmax - x] else paper[y][x]
            xmax = pos - 1
            new_paper = np.zeros([ymax+1,xmax+1])
            for y in range(ymax+1):
                new_paper[y] = paper[y][:xmax+1]
            paper = new_paper
        print(paper)
    print(np.count_nonzero(paper))
    if not part1:
        np.savetxt("part2.csv", paper.astype(int), delimiter="", fmt='%i')

solve(example_input)
solve(problem_input)


solve(problem_input, False)