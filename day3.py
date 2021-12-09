
binary_list = list( map( lambda x: int(x,2)   , 
                open('day3input.txt') ) )

str_list = list(open('day3input.txt') )

print(f"{binary_list[0] = } : {binary_list[0] = :b}")

NUMBER_LEN = 12

one_count = [0] * NUMBER_LEN
zero_count = [0] * NUMBER_LEN
for i in range(NUMBER_LEN):
    for s in str_list:
        one_count[i] += int(s[i])
        zero_count[i] += 1 - int(s[i])

print(f"{one_count =}")
print(f"{zero_count =}")

gamma = [0] * NUMBER_LEN
epsilon = [0] * NUMBER_LEN
for i in range(NUMBER_LEN):
    gamma[i] = 1 if one_count[i] > zero_count[i] else 0
    epsilon[i] = 1 - gamma[i]


print(f"{gamma =}")
print(f"{epsilon =}")

power_consumption = int("".join(map(str,gamma)),2) * \
                    int("".join(map(str,epsilon)),2)
print(f"{power_consumption =}")

#Part 2

def more_common(str_list, index):
    per_index= [s[index] for s in str_list]
    ones = 0
    zeros = 0
    for s in per_index:
        ones += int(s)
        zeros += 1 - int(s)

    assert(per_index.count('0') == zeros)
    assert(per_index.count('1') == ones)

    return 0 if per_index.count('0') > per_index.count('1') else 1

def less_common(str_list, index):
    per_index = [s[index] for s in str_list]
    return 0 if per_index.count('0') <= per_index.count('1') else 1

def rating_finder(str_list, func):
    remaining = str_list.copy()
    for index in range(NUMBER_LEN):
        det_num = func(remaining, index)
        i = len(remaining)-1
        while(i >= 0):
            if (remaining[i][index] != str(det_num)):
                del remaining[i]
            i-=1
        # print(f"{index = } {i = } {len(remaining) = } {det_num = }")
        if len(remaining) <= 1:
            return remaining[0]

    assert(False)

# print([more_common(str_list, i)for i in range(NUMBER_LEN)])

o2 = rating_finder(str_list, more_common)
co2 = rating_finder(str_list, less_common)


print(f"{o2 =}")
print(f"{co2 =}")

life_support_rating = int(o2,2) * int(co2,2)
print(f"{life_support_rating =}")