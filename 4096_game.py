import random
import curses

def initialize_board(size):
    board = [[0] * size for _ in range(size)]
    return board

def print_board(stdscr, board):
    stdscr.clear()
    for i in range(len(board)):
        for j in range(len(board[0])):
            stdscr.addstr(i * 2, j * 6, str(board[i][j]).rjust(5))
    stdscr.refresh()

def add_random_tile(board):
    empty_cells = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])

def is_game_over(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return False
            if i < len(board) - 1 and board[i][j] == board[i + 1][j]:
                return False
            if j < len(board[0]) - 1 and board[i][j] == board[i][j + 1]:
                return False
    return True

def move(board, direction):
    size = len(board)
    if direction == 'left':
        for i in range(size):
            row = board[i]
            board[i] = merge(row)
    elif direction == 'right':
        for i in range(size):
            row = board[i][::-1]
            merged_row = merge(row)
            board[i] = merged_row[::-1]
    elif direction == 'up':
        for j in range(size):
            col = [board[i][j] for i in range(size)]
            merged_col = merge(col)
            for i in range(size):
                board[i][j] = merged_col[i]
    elif direction == 'down':
        for j in range(size):
            col = [board[i][j] for i in range(size)][::-1]
            merged_col = merge(col)
            for i in range(size):
                board[i][j] = merged_col[::-1][i]

def merge(row):
    merged_row = [0] * len(row)
    j = 0
    for i in range(len(row)):
        if row[i] != 0:
            if merged_row[j] == 0:
                merged_row[j] = row[i]
            elif merged_row[j] == row[i]:
                merged_row[j] *= 2
                j += 1
            else:
                j += 1
                merged_row[j] = row[i]
    return merged_row

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    size = 4  # Change this for different game modes
    board = initialize_board(size)
    add_random_tile(board)
    add_random_tile(board)
    
    while True:  # Infinite loop until the user quits
        print_board(stdscr, board)
        direction = stdscr.getch()
        if direction == ord('q'):
            break  # Exit the game when 'q' is pressed
        elif direction in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN]:
            direction_dict = {
                curses.KEY_LEFT: 'left',
                curses.KEY_RIGHT: 'right',
                curses.KEY_UP: 'up',
                curses.KEY_DOWN: 'down'
            }
            move(board, direction_dict[direction])
            add_random_tile(board)
            if is_game_over(board):
                stdscr.addstr(8, 0, "Game Over! You reached 4096! Press 'q' to exit.")
                stdscr.refresh()
                while stdscr.getch() != ord('q'):
                    pass
                break

if __name__ == "__main__":
    curses.wrapper(main)
