def get_input():
    with open('Day_4_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
    board_strings = []
    board_num = -1
    for entry in range(len(raw_input)):
        if entry == 0:
            random_num_strings = raw_input[entry].rstrip('\n').split(',')
            random_nums = []
            for string in random_num_strings:
                random_nums.append(int(string))
        if raw_input[entry] == '\n':
            board_num += 1
        elif raw_input[entry - 1] == '\n':
            board_strings.append(raw_input[entry].rstrip('\n'))
        elif raw_input[entry - 2] == '\n':
            board_strings[board_num] += ' ' + raw_input[entry].rstrip('\n')
        elif raw_input[entry - 3] == '\n':
            board_strings[board_num] += ' ' + raw_input[entry].rstrip('\n')
        elif raw_input[entry - 4] == '\n':
            board_strings[board_num] += ' ' + raw_input[entry].rstrip('\n')
        elif raw_input[entry - 5] == '\n':
            board_strings[board_num] += ' ' + raw_input[entry].rstrip('\n')
    boards = []
    for board in board_strings:
        boards.append(board.split())
    return random_nums, boards

def mark_nums(next_num, boards):
    for board in boards:
        if board.count(str(next_num)) > 0:
            index = board.index(str(next_num))
            board.pop(index)
            board.insert(index, 'X')
    return boards

def check_win(boards):
    for board in boards:
        for i in range(0, 20, 5):
            if board[i] == 'X' and board[i+1] == 'X' and board[i+2] == 'X' and board[i+3] == 'X' and board[i+4] == 'X':
                return board
        for i in range(5):
            if board[i] == 'X' and board[i+5] == 'X' and board[i+10] == 'X' and board[i+15] == 'X' and board[i+20] == 'X':
                return board
    return False

def clear_winners(boards):
    while check_win(boards):
        win_board = check_win(boards)
        index = boards.index(win_board)
        boards.pop(index)
    return boards

def main():
    random_nums, boards = get_input()
    remaining_boards = boards.copy()
    for num in random_nums:
        boards = mark_nums(num, boards)
        if check_win(boards):
            winning_num = num
            break
    winning_board = check_win(boards)
    sum = 0
    for num in winning_board:
        if num == 'X':
            pass
        else:
            sum += int(num)
    print(sum * winning_num)
    for num in random_nums:
        remaining_boards = mark_nums(num, remaining_boards)
        if len(remaining_boards) > 1 and check_win(remaining_boards):
            clear_winners(remaining_boards)
        elif len(remaining_boards) == 1 and check_win(remaining_boards):
            last_num = num
            last_board = check_win(remaining_boards)
            break
    sum = 0
    for num in last_board:
        if num == 'X':
            pass
        else:
            sum += int(num)
    print(sum * last_num)

if __name__ == '__main__':
    main()