day = 22
example_input = f'day{day}example.txt'
problem_input = f'day{day}input.txt'

from parse import parse 
import numpy as np
def solve(input, part2=False):
    cmds = []
    with open(input) as f:
        for line in f:
            val, x1, x2 ,y1, y2, z1, z2 = parse("{} x={:d}..{:d},y={:d}..{:d},z={:d}..{:d}", line.strip()).fixed
            cmds.append((1 if val == "on" else 0, x1, x2 ,y1, y2, z1, z2))
    # print(cmds)

    if part2:
        part2_exp(cmds)
        return

    radius = 50 if not part2 else int(100000/8)

    grid = np.zeros((radius*2,radius*2,radius*2), dtype=bool)

    for i,cmd in enumerate(cmds):
        print(f'{cmd = }')
        val, x1, x2 ,y1, y2, z1, z2 = cmd
        if not part2 and (not range(max(x1, -radius), min(x2, radius)+1) or \
                not range(max(y1, -radius), min(y2, radius)+1) or \
                not range(max(z1, -radius), min(z2, radius)+1)):
            print(i)
            continue
        print(f'{(z2-z1+1)= } ')
        print(f'{(y2-y1+1)= } ')
        print(f'{(x2-x1+1)= } ')
        print(f'{(z2-z1+1) * (y2-y1+1) * (x2-x1+1) = } ')

        grid[z1+radius:z2+radius+1,y1+radius:y2+radius+1,x1+radius:x2+radius+1] = val
        print(f"{np.count_nonzero(grid) = }")
        # print(grid)
    print(np.count_nonzero(grid))


def part2_exp(cmds):
    for i, cmd1 in enumerate(cmds):
        for j, cmd2 in enumerate(cmds):
            if   range(max(cmd1[1], cmd2[1]), min(cmd1[2], cmd2[2])+1) and \
                 range(max(cmd1[3], cmd2[3]), min(cmd1[4], cmd2[4])+1) and \
                 range(max(cmd1[5], cmd2[5]), min(cmd1[6], cmd2[6])+1) and \
                 cmd1[0] != cmd2[0] and i != j:  #Need to have opposite sides
                print(f"Overlap between lines {i+1} and {j+1}")
                print(cmd1)
                print(cmd2)

    on_cubes = 0
    for i, cmd1 in enumerate(cmds):
        for j, cmd2 in enumerate(reversed(cmds[:i])):
            x_overlap = range(max(cmd1[1], cmd2[1]), min(cmd1[2], cmd2[2])+1)
            y_overlap = range(max(cmd1[3], cmd2[3]), min(cmd1[4], cmd2[4])+1)
            z_overlap = range(max(cmd1[5], cmd2[5]), min(cmd1[6], cmd2[6])+1)
            continue
        cubes_impacted = range(cmd1[1],cmd1[2]+1) * range(cmd1[1],cmd1[2]+1) * range(cmd1[1],cmd1[2]+1)

# solve("day22smallexample.txt")
# solve(example_input)
# solve(problem_input)


solve("day22largeexample.txt", True)