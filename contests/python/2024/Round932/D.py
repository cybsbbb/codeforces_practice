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
    n, c = inlt()
    s = inlt()
    s.sort()

    res = (c + 1) * (c) // 2 + c + 1
    even = 0
    odd = 0
    for si in s:
        if si > 2 * c:
            break
        if si % 2 == 0:
            even += 1
        else:
            odd += 1
        if si <= c:
            res -= (si // 2 + 1) + (c - si)
        else:
            res -= (si - c + 1) // 2 + 1
    res += odd * (odd - 1) // 2
    res += even * (even - 1) // 2
    print(res)
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
