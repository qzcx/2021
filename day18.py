day = 18
example_input = f'day{day}example.txt'
problem_input = f'day{day}input.txt'

#Add 
# Nest the two pairs together

#Explode Rules
# left explode val adds to first number to left
# right explode val adds to first number to right
# exploded pair becomes 0

#split
# Becomes a pair
# left <- floor(num/2)
# right <- ceil(num/2)

import ast
def solve(input):
    # l = ast.literal_eval('[[[[4,3],4],4],[7,[[8,4],9]]]')
    # print(l)
    # added_list = add(l, [1,1])
    # print(added_list)
    lines = open(input).readlines()
    list_str = lines[0]
    for line in lines[1:]:
        l1 = ast.literal_eval(list_str)
        l2 = ast.literal_eval(line)
        added_list = add(l1,l2)
        list_str = str(added_list)
        print("ADDED LIST")
        print(added_list)
        reduced_result,list_str = reduce(list_str)
        while(not reduced_result):
            reduced_result, list_str = reduce(list_str)
        print("SUM LIST")
        print(list_str)
    
    print("FINAL LIST")
    print(list_str)
    final_list = ast.literal_eval(list_str)
    print(magnitude(final_list))
    return 

def part2(input):
    mag_list = []
    lines = open(input).readlines()
    for i,line1 in enumerate(lines):
        for j,line2 in enumerate(lines):
            if i == j: continue
            l1 = ast.literal_eval(line1)
            l2 = ast.literal_eval(line2)
            added_list = add(l1,l2)
            list_str = str(added_list)
            # print("ADDED LIST")
            # print(added_list)
            reduced_result,list_str = reduce(list_str)
            while(not reduced_result):
                reduced_result, list_str = reduce(list_str)
            mag_list.append(magnitude(ast.literal_eval(list_str)))
    print(max(mag_list))


import math
def reduce(list_str : str):
    depth = 0
    ex_end = 0
    ex_start = 0
    for idx,c in enumerate(list_str):
        if c == '[':
            depth +=1
            ex_start = idx if depth > 4 else 0
        elif c == ']':
            if depth <= 4:
                depth -=1
            else:
                #explode here
                ex_end = idx
                ex_pair_str = list_str[ex_start:ex_end+1]
                ex_pair = ast.literal_eval(ex_pair_str)
                assert len(ex_pair) == 2
                assert isinstance(ex_pair[0],int)
                assert isinstance(ex_pair[1],int)

                #search left
                l_idx_start = None
                for left_idx in range(ex_start,-1,-1):
                    if l_idx_start is None and list_str[left_idx].isdigit():
                        l_idx_start = left_idx
                    elif l_idx_start is not None and not list_str[left_idx].isdigit():
                        break
                
                #search right
                r_idx_start = None
                for right_idx in range(ex_end,len(list_str)):
                    if r_idx_start is None and list_str[right_idx].isdigit():
                        r_idx_start = right_idx
                    elif r_idx_start is not None and not list_str[right_idx].isdigit():
                        break

                #construct new list
                new_list = ""
                if left_idx != 0:
                    new_list = list_str[:left_idx+1] + \
                            str(int(list_str[left_idx+1:l_idx_start+1]) + ex_pair[0]) + \
                            list_str[l_idx_start+1:ex_start]
                else: 
                    new_list = list_str[:ex_start]
                new_list += '0' #replaces exploded pair with 0
                if right_idx != len(list_str)-1:
                    new_list +=list_str[ex_end+1:r_idx_start] + \
                            str(int(list_str[r_idx_start:right_idx]) + ex_pair[1]) + \
                            list_str[right_idx:]
                else:
                    new_list +=list_str[ex_end+1:]

                # print(f"We exploded {list_str[ex_start:ex_end]} to:")
                # print(new_list)
                return False, new_list
        
    for idx,c in enumerate(list_str):
        if c == '[':
            depth +=1
            ex_start = idx if depth > 4 else 0
        elif c == ']':
            if depth <= 4:
                depth -=1
            else:
                assert(False)
        elif c.isdigit():
            if depth <= 4:
                if list_str[idx+1].isdigit():
                    #reduce here
                    end_idx = idx+1
                    while(list_str[end_idx].isdigit()):
                        end_idx+=1
                    reduce_val = int(list_str[idx:end_idx])
                    new_list = list_str[:idx] + \
                                f"[{int(reduce_val/2)}, {math.ceil(reduce_val/2)}]" + \
                                list_str[end_idx:]
                    # print("We reduced to:")
                    # print(new_list)
                    return False, new_list
            
    return True, list_str


def add(l1,l2):
    return [l1,l2]

def magnitude(l):
    if isinstance(l,list):
        return magnitude(l[0])*3+magnitude(l[1])*2
    else:
        return l

# solve(example_input)
# solve("day18largeexample.txt")
# solve(problem_input)


# part2(example_input)
part2("day18largeexample.txt")
part2(problem_input)