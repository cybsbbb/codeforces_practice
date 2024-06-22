
import collections
import sys
import heapq
import math

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
    k = inlt()
    lcm_tot = math.lcm(*k)
    ans = []
    for ki in k:
        ans.append(lcm_tot // ki)
    if sum(ans) >= lcm_tot:
        print(-1)
    else:
        print(*ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





