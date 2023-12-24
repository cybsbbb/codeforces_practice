import collections
import sys
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


def solution():
    c1, c2, r1, r2 = inlt()
    s, n = inlt()
    m = inp()
    queries = []
    for i in range(m):
        queries.append(inlt())
    res = []
    for x, y in queries:
        # cond 1
        dis = (x - r1) ** 2 + (y - r2) ** 2
        if c1 ** 2 <= dis <= c2 ** 2:
            pass
        else:
            res.append('no')
            continue
        # cond 2
        tmp = 1
        x1, y1 = s, 0
        x2, y2 = n, 500
        tmp *= (x1 - x2) * (y - y2) - (x - x2) * (y1 - y2)
        x1, y1 = s + 100, 0
        x2, y2 = n + 100, 500
        tmp *= (x1 - x2) * (y - y2) - (x - x2) * (y1 - y2)
        if tmp > 0:
            res.append('no')
            continue
        # cond 3
        if 200 < y < 300:
            res.append('no')
            continue
        elif y > 300:
            if y + x > 800:
                res.append('no')
                continue
        elif y < 200:
            if x - y > 300:
                res.append('no')
                continue
        res.append('yes')
        continue

    for ans in res:
        print(ans)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
