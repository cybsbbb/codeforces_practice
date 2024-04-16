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


t = inp()
for _ in range(t):
    x = insr()
    y = insr()
    n = len(x)
    flag = False
    for i in range(n):
        if x[i] == y[i]:
            continue
        else:
            if flag is False:
                if x[i] < y[i]:
                    x[i], y[i] = y[i], x[i]
                flag = True
            else:
                if x[i] > y[i]:
                    x[i], y[i] = y[i], x[i]

    print(''.join(x))
    print(''.join(y))

