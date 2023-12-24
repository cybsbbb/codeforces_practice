import sys
input = sys.stdin.readline


def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def iswin(board):
    # 1 is X win, -1 is O win, 0 is draw or not finished
    for i in range(3):
        # Check row
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                return 1
            if board[i][0] == 'O':
                return -1
        # check col
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                return 1
            if board[0][i] == 'O':
                return -1
    # check diag
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == 'X':
            return 1
        if board[1][1] == 'O':
            return -1
    return 0


def back_tracking(board):
    # Check if finished already
    cur_statas = iswin(board)
    if cur_statas != 0:
        return cur_statas
    # Count X, O number
    x_count = 0
    o_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                x_count += 1
            elif board[i][j] == 'O':
                o_count += 1
    # board already filled
    if x_count + o_count == 9:
        return iswin(board)
    # if next is X
    if x_count == o_count:
        res = -1
        for i in range(3):
            for j in range(3):
                if board[i][j] == '#':
                    board[i][j] = 'X'
                    res = max(res, back_tracking(board))
                    board[i][j] = '#'
        return res
    # if next is O
    if x_count > o_count:
        res = 1
        for i in range(3):
            for j in range(3):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                    res = min(res, back_tracking(board))
                    board[i][j] = '#'
        return res


if __name__ == '__main__':
    board = []
    for i in range(3):
        board.append(insr())

    res = back_tracking(board)
    if res == 1:
        print('Crosses win')
    elif res == 0:
        print('Draw')
    elif res == -1:
        print('Noughts win')




