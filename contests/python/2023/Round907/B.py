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
    n, q = inlt()
    a = inlt()
    q = inlt()
    divided = [[] for i in range(31)]
    for x in q:
        for i in range(1, 31):
            if len(divided[i]) == 0 and i >= x:
                divided[i].append(x)
            if divided[i] and divided[i][-1] > x:
                divided[i].append(x)
    res = []
    for ai in a:
        for j in range(0, 31)[::-1]:
            if ai % (1 << j) == 0:
                ans = ai
                for k in divided[j]:
                    ans += (1 << (k-1))
                res.append(ans)
                break

    print(*res)
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
