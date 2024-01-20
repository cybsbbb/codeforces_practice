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
    n, f, a, b = inlt()
    m = [0] + inlt()
    for i in range(1, n+1):
        cost_a = (m[i] - m[i-1]) * a
        cost_b = b
        cost = min(cost_a, cost_b)
        if f <= cost:
            print("NO")
            return
        f -= cost
    print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
