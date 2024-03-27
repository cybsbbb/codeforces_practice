import sys
import math
import heapq

input = sys.stdin.readline


def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))
def insr():
    s = input()
    return (list(s[:len(s) - 1]))
def invr():
    return (map(int, input().split()))


t = inp()
for i in range(t):
    n, x = inlt()
    a = inlt()

    xor_all = 0
    for ai in a:
        xor_all ^= ai
    if xor_all > x:
        print(-1)
        continue

    def get_res(x):
        res = 0
        cur_xor = 0
        for ai in a:
            cur_xor ^= ai
            if cur_xor | x <= x:
                res += 1
                cur_xor = 0
        if cur_xor != 0:
            res = 0
        return res

    res = get_res(x)

    while x > 0:
        res = max(res, get_res(x - 1))
        x -= x & -x

    print(res)
