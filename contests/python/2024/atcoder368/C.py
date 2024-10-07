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


n = inp()
h = inlt()
t = 0
for hi in h:
    rounds = hi // 5
    t += rounds * 3
    hi -= rounds * 5
    while hi > 0:
        t += 1
        if t % 3 == 0:
            hi -= 3
        else:
            hi -= 1
print(t)
