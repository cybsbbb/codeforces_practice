import collections
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


def op(x, y, op_num):
    if op_num == 0:
        return x + y
    elif op_num == 1:
        return x - y
    elif op_num == 2:
        return x * y
    elif op_num == 3:
        if x % y == 0:
            return x // y
        else:
            return -10000


def smallest_calculated_balue(a, b, c):
    res = 100000
    for i in range(4):
        for j in range(4):
            tmp = (op(op(a, b, i), c, j))
            if tmp >= 0 and tmp < res:
                res = tmp
    print(res)


if __name__ == '__main__':
    a, b, c = inlt()
    smallest_calculated_balue(a, b, c)
