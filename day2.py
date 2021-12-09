

def input_parse(line):
    splits = line.split(' ')
    return splits[0], int(splits[1].strip())


commands = list(map(input_parse, 
                    open('./day2input.txt')))

#print(commands)

import pandas as pd

df = pd.DataFrame(columns=['h_pos','d_pos'])

h_pos = 0
d_pos = 0
for com in commands:
    if com[0] == 'forward':
        h_pos += com[1]
    elif com[0] == 'down':
        d_pos += com[1]
    elif com[0] == 'up':
        d_pos -= com[1]
    df = df.append({'h_pos':h_pos,'d_pos': -1*d_pos}, 
                ignore_index=True)

# print(df.head())


import matplotlib
lines = df.plot.line(x='h_pos', y='d_pos')

lines.get_figure().savefig('part1')

# print(f" h_pos {h_pos} d_pos {d_pos} prod {h_pos*d_pos}")

# #Part 2

aim = 0
h_pos = 0
d_pos = 0
df = pd.DataFrame(columns=['h_pos','d_pos'])
for com in commands:
    if com[0] == 'forward':
        h_pos += com[1]
        d_pos += aim * com[1]
    elif com[0] == 'down':
        aim += com[1]
    elif com[0] == 'up':
        aim -= com[1]
    df = df.append({'h_pos':h_pos,'d_pos': -1*d_pos}, 
                ignore_index=True)

print(df.head())


lines = df.plot.line(x='h_pos', y='d_pos')
lines.get_figure().savefig('part2')

# print(f"""PART 2 
#     h_pos {h_pos} 
#     d_pos {d_pos} 
#     aim {aim} 
#     prod {h_pos*d_pos}""")
