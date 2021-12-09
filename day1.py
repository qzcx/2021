

#Part 1
with open('day1input.txt') as in_file:
    count = 0
    prev = None
    for line in in_file:
        cur =  int(line.strip())
        if prev != None and cur > prev:
            count+=1
        prev = cur

print(count)

#PART 2
import sys
with open('day1input.txt') as in_file:
    count = 0
    prev = None
    window = []
    for line in in_file:
        window.append(int(line.strip()))
        if len(window) < 3:
            continue
        if len(window) > 3:
            window.pop(0)
        
        print(window)
        cur =  sum(window)
        if prev != None and cur > prev:
            count+=1
        prev = cur

print(count)