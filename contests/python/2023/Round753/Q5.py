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

def robotOnTheBoard():
    n, m = inlt()
    moves = insr()
    lm, rm, dm, um = 0, 0, 0, 0
    x, y = 0, 0
    ret_x, ret_y = 1, 1
    for move in moves:
        if move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
        elif move == 'D':
            y -= 1
        elif move == 'U':
            y += 1
        lm = min(lm, x)
        rm = max(rm, x)
        dm = min(dm, y)
        um = max(um, y)

        if rm - lm + 1 > m or um - dm + 1 > n:
            break

        ret_x, ret_y = -lm + 1, um + 1

    print(ret_y, ret_x)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        robotOnTheBoard()

