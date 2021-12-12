day = 11
example_input = f'day{day}example.txt'
problem_input = f'day{day}input.txt'
import numpy

def solve(input, part2 = False):
    octpi = list(map(lambda x: list(map( int, list(x.strip()))),open(input) ))
    octpi = numpy.array(octpi)
    print(octpi)
    width = len(octpi[0])
    height = len(octpi)

    flashes = 0
    steps = 100 if not part2 else 10000
    for i in range(steps):
        #increase all octpi by 1
        octpi += 1
        for y in range(height):
            for x in range(width):
                if octpi[y][x] > 9:
                    flashes += 1
                    octpi[y][x] = -1
                    flashes += flash(x,y, octpi)
        if(numpy.all(octpi == -1)):
            print("Part 2", i)
            return
        octpi[octpi == -1] = 0

    print(flashes)

def flash(x, y, octpi):
    # print(f'{x} {y}')
    width = len(octpi[0])
    height = len(octpi)
    neighbors = [ (x-1,y-1), (x-1,y), (x,y-1), (x+1,y+1), (x+1,y), (x,y+1), (x-1,y+1), (x+1,y-1)]
    flashes = 0
    for x_,y_ in neighbors:
        if x_ >= width or x_ < 0 or y_ >=height or y_<0:
            continue
        octpi[y_][x_] += 1 if octpi[y_][x_] != -1 else 0
        if octpi[y_][x_] > 9:
            flashes += 1
            octpi[y_][x_] = -1
            flashes += flash(x_,y_, octpi)
    return flashes



solve(example_input)
solve(problem_input)

solve(example_input, True)
solve(problem_input, True)

print("Finished")