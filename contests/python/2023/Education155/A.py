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
    n = inp()
    athletes = []
    for i in range(n):
        athletes.append(inlt())
    Polycarp_s, Polycarp_e = athletes[0]
    res = 1
    for i in range(1, n):
        sub_s, sub_e = athletes[i]
        if sub_e >= Polycarp_e:
            res = max(res, sub_s + 1)
    if res > Polycarp_s:
        print(-1)
    else:
        print(res)

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
