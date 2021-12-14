day = 14
example_input = f'day{day}example.txt'
problem_input = f'day{day}input.txt'

import numpy as np
import pandas as pd
from functools import lru_cache 

def solve(input, steps=10):
    manual = list(map(lambda x: list(x.strip().split(' -> ')), open(input) ) )
    template = list(list(filter(lambda x: len(x) == 1 and x[0] != '', manual))[0][0])
    
    global pairs
    pairs = dict( filter(lambda x: len(x) == 2, manual) )#Filter each list to just the points
    print(template)
    print(f'{pairs = }')

    # template_new = template.copy() 
    # print("".join(template))
    template = "".join(template)

    cur_pairs = {}
    for i in range(len(template)-1):
        substr = template[i:i+2]
        cur_pairs[substr] = 1 if substr not in cur_pairs else cur_pairs[substr]+1

    for n in range(steps):
        new_pairs = {}
        for substr in cur_pairs:
            if substr in pairs:
                new_strings = [substr[0] + pairs[substr], pairs[substr] + substr[1]]
            else:
                new_strings = [substr]
            for n in new_strings:
                new_pairs[n] = cur_pairs[substr] if n not in new_pairs else new_pairs[n]+cur_pairs[substr]
        cur_pairs = new_pairs
    # print(cur_pairs)
    # print(f'{sum(cur_pairs.items(), key=lambda x: x[1])}')
    counts = {}
    for p, c in cur_pairs.items():
        for char in p:
            counts[char] = c if char not in counts else counts[char]+c

    min_val = min(counts.items(), key=lambda x: x[1])
    max_val = max(counts.items(), key=lambda x: x[1])
    print(f'{min_val =}')
    print(f'{max_val = }')
    import math
    print(f'{math.ceil(max_val[1]/2) - math.ceil(min_val[1]/2)= }')
    # occurances = pd.Series(list(template)).value_counts()
    # print(occurances)
    # print(f'{occurances[occurances.idxmax()] - occurances[occurances.idxmin()] = }')
    # print("".join(template))




solve(example_input)
solve(problem_input)


solve(example_input, 40)
solve(problem_input, 40)


#BAD SOLUTIONS

    # for n in range(steps):
        # template = pair_insertion(template)
        #inefficent version
        # insert_point=1
        # for i in range(len(template)-1):
        #     substr = "".join(template[i:i+2])
        #     if substr in pairs:
        #         template_new.insert(insert_point, pairs[substr])
        #         insert_point+=1
        #     insert_point+=1
        # template = template_new.copy()
        # print(template)

        #still not good enough
# @lru_cache
# def pair_insertion(substr):
#     global pairs
#     if len(substr) == 1:
#         return substr
#     if len(substr) == 2:
#         if substr in pairs:
#             return "".join([substr[0],pairs[substr],substr[1]])
#         else:
#             return substr
#     else:
#         halfway = int(len(substr)/2)
#         mid_point = substr[halfway-1:halfway+1]
#         mid_result = pair_insertion(pairs[mid_point]) if mid_point in pairs else ""
#         return "".join([pair_insertion(substr[:halfway]), 
#                         mid_result,
#                         pair_insertion(substr[halfway:])])