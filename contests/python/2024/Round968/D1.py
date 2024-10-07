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
    n, m = inlt()
    max_reachable = 0
    for _ in range(n):
        a = inlt()
        a_set = set(a[1:])
        flag = False
        first = -1
        second = -1
        for i in range(2 * 10 ** 5 + 5):
            if i not in a_set:
                if flag is False:
                    first = i
                    flag = True
                else:
                    second = i
                    break
        max_reachable = max(max_reachable, second)

    ans = 0
    ans += max_reachable * (min(m, max_reachable) + 1)
    if m > max_reachable:
        ans += (max_reachable + 1 + m) * (m - max_reachable) // 2
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





