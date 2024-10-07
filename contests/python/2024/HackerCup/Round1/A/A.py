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


def solution(ttt):
    n = inp()
    min_v = 0
    max_v = float('inf')
    for t in range(1, n + 1):
        ai, bi = inlt()
        if ai > 0:
            max_v = min(max_v, t / ai)
        if bi > 0:
            min_v = max(min_v, t / bi)

    if min_v > max_v or min_v == 0:
        print(f"Case #{ttt}: {-1}")
    else:
        print(f"Case #{ttt}: {min_v}")
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution(i + 1)
