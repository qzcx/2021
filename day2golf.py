# def input_parse(line):
#     splits = line.split(' ')
#     return splits[0], int(splits[1].strip())

coms = list(map(lambda line: line.split(' '), 
                open('./day2input.txt')))

map(lambda a,b: ,
    coms)

h_pos = 0
d_pos = 0
for c in coms:
    if c[0][0]=='f':
        h_pos+=int(c[1])