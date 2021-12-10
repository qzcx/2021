day = 10
example_input = f'day{day}example.txt'
problem_input = f'day{day}input.txt'

def solve(input):
    open_chars = ['(', '[', '{', '<' ]
    close_chars = [')', ']', '}', '>']
    mapping = {'(':')', '[':']', '{':'}', '<':'>'}
    rewards  = {')': 3, ']' : 57 ,'}' : 1197 ,'>': 25137, #Part 1 rewards
                '(':1, '[':2, '{':3, '<':4} #Part 2 rewards
    lines = list(map(lambda x: x.strip(), open(input)))
    # print(lines)
    points = 0
    points2 = []
    for line in lines:
        stack = []
        err = False
        for c in line:
            if c in open_chars:
                stack.append(c)
            elif c in close_chars:
                if len(stack) == 0 or mapping[stack.pop()] != c:
                    points += rewards[c]
                    err = True
                    break
            else:
                assert(False)
        # assert(len(stack) == 0)
        line_points = 0
        if err or len(stack) == 0:
            continue
        while(len(stack) != 0):
            c = stack.pop()
            line_points = line_points*5 + rewards[c]
        points2.append(line_points)
        
    print(f'{points =}')

    points2.sort()
    import math
    print(f'{points2[math.floor(len(points2)/2)] }')

solve(example_input)
solve(problem_input)