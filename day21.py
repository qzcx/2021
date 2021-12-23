day = 21
example_input = f'day{day}example.txt'
problem_input = f'day{day}input.txt'



scores = [0,0]
def solve(p1,p2):
    global scores, pos
    pos = [p1-1,p2-1]
    turn_count = 0
    while(max(scores) < 1000):
        turn = turn_count % 2
        roll = dice_roll() + dice_roll() + dice_roll()
        pos[turn] = (roll + pos[turn]) % 10
        scores[turn] +=  pos[turn] + 1 #add one to convert to 1 index
        turn_count += 1 
        # print(f"{scores = } {turn = } {pos[turn] = }")
    print(f"{scores = }")
    print(f"{turn_count = }")
    print(f"{min(scores) * (turn_count*3) = }")

last_roll = 100
def dice_roll(part1=True):
    global last_roll
    last_roll = (last_roll+1) %100
    return last_roll

import numpy as np
def roll_dirac_options():
    a = np.zeros((3*3*3), dtype=int)
    c =0
    for d1 in range(1,4):
        for d2 in range(1,4):
            for d3 in range(1,4):
                a[c] = (d1+d2+d3)
                c+=1
    (unique, counts) = np.unique(a, return_counts=True)
    frequencies = np.asarray((unique, counts)).T
    # print(np.unique(a, True))
    print(frequencies)
    return frequencies


#Each turn has 3*3*3 possible rolls, but only 1-9 possible values. 
    #3:1, 4:3, 5:
# [3., 4., 5., 6., 7., 8., 9.]), 
# [ 0,  1,  2,  5,  8, 17, 26]

#Each player can play individually?
    #Calculate the number of turns to win from each position
    #Compare number of turns per player against each other to determine how often they win with that set

dice_freq = roll_dirac_options()
#return the count of times to win from this position
def number_of_turns_to_win(cur_pos, score, cur_turn):
    global dice_freq
    win_turn = [0]*10
    for val, multiplier in dice_freq:
        new_pos = (cur_pos + val)%10
        new_score = score + new_pos + 1
        if new_score >=21:
            win_turn[cur_turn] += 1* multiplier
        else:
            new_win_turn = number_of_turns_to_win(new_pos, new_score, cur_turn+1)
            win_turn = [x+x2*multiplier for x,x2 in zip(win_turn, new_win_turn)]
    return win_turn

def number_of_turns_to_win2(cur_pos, score, cur_turn, p):
    global dice_freq
    win_turn = [[0]*10,[0]*10]
    for val, multiplier in dice_freq:
        new_pos = cur_pos.copy()
        new_pos[p] = (cur_pos[p] + val)%10
        new_score = score.copy()
        new_score[p] = score[p] + new_pos[p] + 1
        if new_score[p] >=21:
            win_turn[p][cur_turn] += 1* multiplier
        else:
            new_win_turn = number_of_turns_to_win2(new_pos, new_score, cur_turn+p, (p+1)%2 )
            win_turn = [[x+x2*multiplier for x,x2 in zip(win_turn[0], new_win_turn[0])],
                        [x+x2*multiplier for x,x2 in zip(win_turn[1], new_win_turn[1])]]
    return win_turn

from functools import cache

@cache
def number_of_turns_to_win3(p0, p1, p0s, p1s, p): #10 * 10 * 21 * 21 * 2
    global dice_freq
    wins = 0
    for val, multiplier in dice_freq:
        if p == 0:
            new_p0 = (p0 + val)%10
            new_p0s = p0s + new_p0 + 1
            if new_p0s >=21:
                wins += multiplier
            else:
                wins += multiplier*number_of_turns_to_win3(new_p0, p1, new_p0s, p1s, (p+1)%2 )
        else:
            new_p1 = (p1 + val)%10
            new_p1s = p1s + new_p1 + 1
            if new_p1s >=21:
                wins += multiplier*1j
            else:
                wins += multiplier*number_of_turns_to_win3(p0, new_p1, p0s, new_p1s, (p+1)%2 )
    return wins

# p1_turns_to_win,p2_turns_to_win = number_of_turns_to_win3(0, 0, 0, 21, 0)

# print(f"{p1_turns_to_win = }")
# print(f"{p2_turns_to_win = }")

def part2(p1,p2):
    wins = number_of_turns_to_win3(p1-1, p2-1, 0, 0, 0)
    print(f'{wins.real = }, {wins.imag = }, {int(max(wins.real, wins.imag)) = }')
    # p1_turns_to_win = number_of_turns_to_win(p1-1, 0, 0)
    # p2_turns_to_win = number_of_turns_to_win(p2-1, 0, 0)

    # print(f"{p1_turns_to_win = }")
    # print(f"{p2_turns_to_win = }")

    # print("p1")
    # print(times_won(p1_turns_to_win,p2_turns_to_win))
    # print("p2")
    # print(times_won(p2_turns_to_win[:-1],p1_turns_to_win[1:]))

# [2, 1, 1]
#     x
# [2, 1, 1]

# 4 times for 1 turns
# 2 times for 2 turns
# 1 time  for 3 turns

def times_won(p1_turns_to_win,p2_turns_to_win):
    times_won = 0
    for i,val in enumerate(p1_turns_to_win):
        times_won += val * sum(p2_turns_to_win[i:])
    return times_won

    
# def go_turn():
    # number of wins for this turn
        #7 possibilites for a turn


# solve(4,8)
# solve("day18largeexample.txt")
# solve(6,1)
# roll_dirac_options()

part2(4,8)
part2(6,1)