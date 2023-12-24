import math
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


if __name__ == '__main__':
    x, y, x1, y1, x2, y2 = inlt()
    res = 0
    if x2 >= x >= x1:
        res = float(min(abs(y1-y), abs(y2-y)))
    elif y2 >= y >= y1:
        res = float(min(abs(x1 - x), abs(x2 - x)))
    else:
        n1 = (x1 - x)**2 + (y1 - y)**2
        n2 = (x1 - x) ** 2 + (y2 - y) ** 2
        n3 = (x2 - x) ** 2 + (y1 - y) ** 2
        n4 = (x2 - x) ** 2 + (y2 - y) ** 2
        res = math.sqrt(min(n1, n2, n3, n4))

    print("{:.3f}".format(res))


