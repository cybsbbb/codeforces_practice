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
    a = inlt()
    b = inlt()
    a_continues = collections.defaultdict(int)
    b_continues = collections.defaultdict(int)

    # A
    cur = a[0]
    cur_len = 1
    for i in range(1, n):
        if a[i] == cur:
            cur_len += 1
        else:
            a_continues[cur] = max(a_continues[cur], cur_len)
            cur = a[i]
            cur_len = 1
    a_continues[cur] = max(a_continues[cur], cur_len)

    # B
    cur = b[0]
    cur_len = 1
    for i in range(1, n):
        if b[i] == cur:
            cur_len += 1
        else:
            b_continues[cur] = max(b_continues[cur], cur_len)
            cur = b[i]
            cur_len = 1
    b_continues[cur] = max(b_continues[cur], cur_len)

    res = 0
    for key in a_continues.keys() | b_continues.keys():
        res = max(res, a_continues[key] + b_continues[key])

    print(res)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
