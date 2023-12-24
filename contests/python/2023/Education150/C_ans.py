import sys
import math
import collections
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


def id(c):
    return ord(c) - ord('A')


def evaluate(s):
    res = 0
    max_id = -1
    for x in s[::-1]:
        i = id(x)
        if max_id > i:
            res -= 10 ** i
        else:
            res += 10 ** i
        max_id = max(max_id, i)
    return res


def solution():
    s = insr()
    res = -float('inf')
    for x in ['A', 'B', 'C', 'D', 'E']:
        for y in ['A', 'B', 'C', 'D', 'E']:
            if not (x in s):
                continue
            idx_l = s.index(x)
            idx_r = len(s) - s[::-1].index(x) - 1
            s[idx_l] = y
            res = max(res, evaluate(s))
            s[idx_l] = x
            s[idx_r] = y
            res = max(res, evaluate(s))
            s[idx_r] = x

    print(res)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
