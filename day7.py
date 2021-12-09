
example_input = 'day7example.txt'
problem_input = 'day7input.txt'

def fuel_cost(pos, goal_pos):
    return abs(pos - goal_pos)

def fuel_cost2(pos, goal_pos):
    num_steps = fuel_cost(pos, goal_pos)
    cost = 0
    return (num_steps * num_steps) / 2
    return sum(range(1,num_steps+1))

import statistics

def solve(input, part2=False):
    crabs = list(map(lambda x: x.strip().split(','), open(input)))[0]
    crabs = list(map(int,crabs))
    # print(crabs)
    m = min(crabs)
    M = max(crabs)
    print(f'{m =} {M =} {statistics.mean(crabs) = } {statistics.median(crabs) = }')
    pos_costs = []
    for i in range(0,M):
        costs = 0
        for c in crabs:
            costs += fuel_cost(c, i) if not part2 else fuel_cost2(c, i)
        pos_costs.append(costs)

    print(f'{min(pos_costs) =} {pos_costs.index(min(pos_costs)) = }')

solve(example_input)
solve(problem_input)

solve(example_input, True)
solve(problem_input, True)