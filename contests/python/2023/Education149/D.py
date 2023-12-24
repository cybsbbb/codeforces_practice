import collections
import sys
import math
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


def solution():
    n = inp()
    s = insr()
    res = []
    cur_value = 0
    cur_symbol = 0
    if s[0] == '(':
        cur_value = 1
        cur_symbol = 1
        res.append(1)
    elif s[0] == ')':
        cur_value = -1
        cur_symbol = -1
        res.append(2)
    for i in range(1, n):
        if s[i] == '(':
            cur_value += 1
        elif s[i] == ')':
            cur_value -= 1

        if cur_value == 0:
            res.append(res[-1])
        elif cur_value > 0 and cur_symbol > 0:
            res.append(res[-1])
        elif cur_value < 0 and cur_symbol < 0:
            res.append(res[-1])
        elif cur_value < 0 and cur_symbol > 0:
            cur_symbol = -1
            res.append(2)
        elif cur_value > 0 and cur_symbol < 0:
            cur_symbol = 1
            res.append(1)

    if cur_value != 0:
        print(-1)
        return
    else:
        num_color = len(set(res))
        if num_color == 2:
            print(len(set(res)))
            print(' '.join(map(str, res)))
        elif num_color == 1 and res[0] == 2:
            print(len(set(res)))
            print(' '.join(map(lambda x: str(x-1), res)))
        elif num_color == 1 and res[0] == 1:
            print(len(set(res)))
            print(' '.join(map(str, res)))

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
