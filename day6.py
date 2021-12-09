
example_input = 'day6example.txt'
problem_input = 'day6input.txt'


cur_day = 0

#offset : number of fish at this offset

def init_fishes(init_list):
    fishes = [0] * 7
    for fish in init_list:
        fishes[int(fish)] +=1
    return fishes

def solve(input, days=80):
    upcoming_fish = [0, 0]
    init_list = list(map(lambda x: x.split(','), open(input) ) )[0]
    fishes = init_fishes(init_list)
    print(fishes)
    for n in range(days):
        step_one_day(fishes, n, upcoming_fish)
    print(f'{sum(fishes) = } + {sum(upcoming_fish) =}')
    print(f'{sum(fishes) + sum(upcoming_fish) =}')

#Starts with two fish in queue
def step_one_day(fishes, cur_day, upcoming_fish):
    cycle_day = cur_day % 7
    upcoming_fish.append(fishes[cycle_day])
    fishes[cycle_day] += upcoming_fish.pop(0)
    # print(f'{cur_day = } {cycle_day = } : {fishes =}')

#Part1
solve(example_input, 18)
solve(example_input, 80)
solve(problem_input, 80)


solve(example_input, 256)
solve(problem_input, 256)