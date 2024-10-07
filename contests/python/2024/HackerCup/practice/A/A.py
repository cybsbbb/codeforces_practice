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


def solution(t):
    n, k = inlt()
    s = []
    for _ in range(n):
        s.append(inp())
    if n == 1:
        if s[0] <= k:
            print(f"Case #{t}: YES")
            return
        else:
            print(f"Case #{t}: NO")
            return
    min_s = min(s)
    if min_s * (2 * n - 3) <= k:
        print(f"Case #{t}: YES")
        return
    else:
        print(f"Case #{t}: NO")
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution(i + 1)
