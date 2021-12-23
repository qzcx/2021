day = 22
example_input = f'day{day}example.txt'
problem_input = f'day{day}input.txt'

# from parse import parse 
# import numpy as np
def solve(input, part2=False):
    cubes = []
    xs = []
    ys = []
    zs = []
    with open(input) as f:
        for line_num,line in enumerate(f):
            # val, x1, x2 ,y1, y2, z1, z2 = parse("{} x={:d}..{:d},y={:d}..{:d},z={:d}..{:d}", line.strip()).fixed
            val, positions = line.split()
            x, y, z = positions.split(",")
            x1, x2 = map(int, x.split("=")[1].split(".."))
            y1, y2 = map(int, y.split("=")[1].split(".."))
            z1, z2 = map(int, z.split("=")[1].split(".."))
            cubes.append( (1 if val == "on" else 0, (x1, x2+1) ,(y1, y2+1), (z1, z2+1) ))
            xs.append(x1)
            xs.append(x2+1)
            ys.append(y1)
            ys.append(y2+1)
            zs.append(z1)
            zs.append(z2+1)

    #https://www.reddit.com/r/adventofcode/comments/rmivfy/everyone_is_overcomplicating_day_22/
    xs.sort()
    ys.sort()
    zs.sort()
    # cubes.reverse()

    count = 0
    for x1,x2 in zip(xs,xs[1:]):
        x_cubes = [cube for cube in cubes if cube[1][0] <= x1 < cube[1][1]]
        if len(x_cubes) == 0: continue
        for y1,y2 in zip(ys,ys[1:]):
            y_cubes = [cube for cube in x_cubes if cube[2][0] <= y1 < cube[2][1]]
            if len(y_cubes) == 0: continue
            for z1,z2 in zip(zs,zs[1:]):
                for cube in reversed(y_cubes):
                    if cube[3][0] <= z1 < cube[3][1]:
                        count += (x2-x1) * (y2-y1) * (z2-z1) if cube[0] else 0
                        break
    print(count)

solve("day22largeexample.txt", True)
solve(problem_input)

    # for line_num, cmd in enumerate(cmds[:-1]):
    #     x_overlap, y_overlap, z_overlap = get_intersection(cmd, cmds[-1]) 
    #     if  x_overlap and y_overlap and z_overlap:
    #         print(f"Line {line_num} is partially consumed by the last off")
    #         print(f"{cmd = }")
    #         print(f"{x_overlap = }")
    #         print(f"{y_overlap = }")
    #         print(f"{z_overlap = }")
        
    #     if  is_fully_overlapped(cmd, cmds[-1]):
    #         print(f"Line {line_num} is fully consumed by the last off")
#     print(f"{cmds[-1] = }")


# def check_range_on(point, cubes):
#     for cube in cubes:
#         if cube[0] == 1:
#             continue
#         elif point[0] in cube[1] and  point[1] in cube[2] and  point[2] in cube[3]:
#             return False
#     return True

# def get_intersection(cube1, cube2):
#     x_overlap = range(max(cube1[1], cube2[1]), min(cube1[2], cube2[2])+1)
#     y_overlap = range(max(cube1[3], cube2[3]), min(cube1[4], cube2[4])+1)
#     z_overlap = range(max(cube1[5], cube2[5]), min(cube1[6], cube2[6])+1)
#     return (x_overlap, y_overlap, z_overlap)

# #Check if cube1 is fully overlapped by cube2
# def is_fully_overlapped(cube1, cube2):
#     (x_overlap, y_overlap, z_overlap) = get_intersection(cube1, cube2)
#     if x_overlap and y_overlap and z_overlap and \
#        x_overlap[0] == cube1[1] and x_overlap[-1] == cube1[2] and  \
#        y_overlap[0] == cube1[3] and y_overlap[-1] == cube1[4] and \
#        z_overlap[0] == cube1[5] and z_overlap[-1] == cube1[6]:
#        return True
#     return False




# solve("day22largeexample.txt", True)
# solve(problem_input)

"""
Track cubes of "on" sections

Start with first cuboid. Add it to "on" cube list

Take next cuboid. Check for overlap with "on" list
    Cmd is "on", add it to the "on" list (Add area to on_count)

    If overlap determine the difference. 
        If cmd is "on" then save the overlap in overlap list. (subtract overlap area from on_count)
        If cmd is "off" 
            Check for overlap with existing "off" list
            then save overlap to the "off" list (subtract overlap area from on_count)


"""