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


def Maze():
    n, m = inlt()
    x1, y1, x2, y2 = inlt()

    if (x1 == 1 and y1 == 1) or (x1 == 1 and y1 == m) or (x1 == n and y1 == 1) or (x1 == n and y1 == m) or \
        (x2 == 1 and y2 == 1) or (x2 == 1 and y2 == m) or (x2 == n and y2 == 1) or (x2 == n and y2 == m):
        print(2)
    elif x1 == 1 or x1 == n or y1 == 1 or y1 == m or x2 == 1 or x2 == n or y2 == 1 or y2 == m:
        print(3)
    else:
        print(4)

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        Maze()
