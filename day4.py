# board = {'nums':[[]], 'marks':[[]], 'won': False}

#generate boards
def read_input():
    #first line is list of numbers
    # in_file = 'day4example.txt' 
    in_file = 'day4input.txt' 
    input = list(open(in_file))
    bingo_nums = list(map(int, input[0].strip().split(',') ) )

    boards = []
    for i in range(1,len(input),6):
        board = { 'nums':[], 'marks': [[0]*5 for i in range(5)] , 'won': False}
        for line in input[i+1:i+6]:
            board["nums"].append( list( map(int, line.strip().split()) ))
        boards.append(board)
    return bingo_nums, boards

#Updates the passed in board
def mark_board(board, num):
    for x,row in enumerate(board['nums']):
        for y,cell in enumerate(row):
            if cell == num:
                board['marks'][x][y] = 1

#Return True if winner
def check_board(board):
    for x in range(5):
        col_check = 1
        row_check = 1
        for y in range(5):
            col_check *= board['marks'][x][y]
            row_check *= board['marks'][y][x]
        if col_check == 1 or row_check == 1:
            return True
    return False

#Return the sum of the unmarked numbers
def score_board(board):
    s = 0
    for x,row in enumerate(board['nums']):
        for y,cell in enumerate(row):
            s += cell if board['marks'][x][y] == 0 else 0
    return s

bingo_nums, boards = read_input()

# print(f'{bingo_nums = }')
# print(f'{boards = }')
def run_game():
    count_won_boards = 0
    for i,num in enumerate(bingo_nums):
        for board in boards:
            mark_board(board, num)
            if not board['won'] and check_board(board):
                count_won_boards+= 1
                board['won'] =  True
                if (count_won_boards == 1):
                    score = score_board(board) 
                    print(f'PART 1 {score = } {num = } {score*num = }')
                elif(count_won_boards == len(boards)):
                    score = score_board(board) 
                    print(f' PART 2 {score = } {num = } {score*num = }')

run_game()
            


#Part 2

