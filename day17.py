day = 17
example_input = f'day{day}example.txt'
problem_input = f'day{day}input.txt'

from os import devnull
from parse import search,parse 

def solve(input):
    parse_result = parse("target area: x={}..{}, y={}..{}", open(input).readline())
    xmin, xmax, ymin, ymax = parse_result.fixed
    print(f"{xmin = }, {xmax = }, {ymin = }, {ymax = }")
    yresults = part1(int(ymin),int(ymax))
    xresults = part2(int(xmin),int(xmax))
    # print(f"{yresults = }\n {xresults = }")
    print(f"{len(yresults) = } {len(xresults) = }")
    # print(f"{len(y_results) * len(x_results) = }")
    # check_options(int(xmin), int(xmax), int(ymin), int(ymax), [6], [8])
    check_options(int(xmin), int(xmax), int(ymin), int(ymax), xresults, yresults)

def part1(ymin,ymax):
    results = []
    for ytest in range(ymin,1000): #Is ymin the best start?
        ypos = 0
        yvel = ytest
        y_best_max = 0
        while(ypos > ymin and (ypos not in range(ymin,ymax+1) or yvel > 0)):
            ypos,yvel = y_step(ypos,yvel)
            y_best_max = ypos if yvel >= 0 else y_best_max
        if ypos in range(ymin,ymax+1):
            results.append((y_best_max,ytest))
    print(max(results))
    return [r[1] for r in results]

def part2(xmin, xmax):
    results = []
    for xtest in range(1,xmax+1): #Is xmin the best start?
        xpos = 0
        xvel = xtest
        while(xpos < xmin and xpos not in range(xmin,xmax+1) and xvel > 0):
            xpos,xvel = x_step(xpos,xvel)
        if xpos in range(xmin,xmax+1):
            results.append((xtest))
    return results

def check_options(xmin, xmax, ymin, ymax, xresults, yresults):
    combos = [(x,y) for x in xresults for y in yresults]
    results = []
    for (xtest,ytest) in combos:
        xpos = ypos = 0
        yvel = ytest
        xvel = xtest
        while not (ypos in range(ymin,ymax+1) and xpos in range(xmin,xmax+1)):
            if xpos > xmax or (xpos < xmin and xvel == 0):
                break
            if ypos < ymin:
                break
            ypos,yvel = y_step(ypos,yvel)
            xpos,xvel = x_step(xpos,xvel)
        if xpos in range(xmin,xmax+1) and ypos in range(ymin,ymax+1):
            results.append((xtest,ytest))

    # print(f" Part 2 {results = }")
    print(f"{len(results) = }")

def x_step(pos, vel):
    # The probe's y position increases by its y velocity.    
    # Due to gravity, the probe's y velocity decreases by 1.
    return pos+vel, vel-1 if vel != 0 else vel

def y_step(pos, vel):
    # The probe's y position increases by its y velocity.    
    # Due to gravity, the probe's y velocity decreases by 1.
    return pos+vel, vel-1

# def step():
    # The probe's x position increases by its x velocity.
    # Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.


    
solve(example_input)
solve(problem_input)