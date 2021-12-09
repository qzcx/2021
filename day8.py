example_input = 'day8example.txt'
problem_input = 'day8input.txt'

def solve(input, part2=False):
    patterns = []
    outputs = []
    with open(input) as f:
        for line in f:
            # print(f'{line.strip().split("|") = }')
            (pattern, output) = line.strip().split('|')
            patterns.append(pattern.split(' '))
            outputs.append(output.strip().split(' '))

    #Part 1 - find 1,4,7,8
    count = 0
    for output in outputs:
        for word in output:
            # print(f'{word = }')
            if len(word) in [2,3,4,7]:
                count+=1
    print(count)

    #Part 2
    results = []
    for i in range(len(patterns)):
        results.append(solve_line(patterns[i], outputs[i]))
    print(f'{results = }, {sum(results) = }')

def solve_line(patterns, outputs):
    patterns = list(map(lambda x: set(list(x)), patterns))
    outputs = list(map(lambda x: set(list(x.strip())), outputs))
    print(f'{patterns = } {outputs = }')
    #identify easy numbers
    five_len = []
    six_len = []
    #sort by segment length, label known numbers
    for p in patterns:
        if len(p) == 2:
            one = p
        elif len(p) == 3:
            seven = p
        elif len(p) == 4:
            four = p
        elif len(p) == 5:
            five_len.append(p) #5,2,3
        elif len(p) == 6:
            six_len.append(p) #zero, six, nine
        elif len(p) == 7:
            eight = p
    
    # top, tl, tr, mid, bl, br, bot
    # top = seven.intersection(five_len)
    for s in six_len:
        if len(four.intersection(s)) == 4:
            nine = s
        else:
            if len(one.intersection(s)) == 2:
                zero = s
            else:
                six = s

    bl = zero.difference(nine)

    for f in five_len: #5,2,3
        if len(six.intersection(f)) == 5:
            five = f
        elif len(bl.intersection(f)) != 1:
            three = f
        else:
            two = f

    decoder = [(zero,0), (one,1), (two,2), (three,3), (four,4), (five,5), (six,6), (seven,7), (eight,8), (nine,9)]
    result = 0
    digit = 1000
    
    for o in outputs:
        for d,val in decoder:
            if o == d:
                break
        result += val * int(digit)
        digit /= 10

    return result
    

solve(example_input)
solve(problem_input)
