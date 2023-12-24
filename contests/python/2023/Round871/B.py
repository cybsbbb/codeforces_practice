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


def BlankSpace():
    n = inp()
    arr = inlt()
    res = 0
    tmp_max = 0
    for i in range(n):
        if arr[i] == 0:
            tmp_max += 1
        else:
            res = max(res, tmp_max)
            tmp_max = 0
    res = max(res, tmp_max)
    print(res)
    return res


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        BlankSpace()
