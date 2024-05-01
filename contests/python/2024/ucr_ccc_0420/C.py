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
    n, k = inlt()
    a = collections.deque(inlt())
    ans = 0
    while a and k > 0:
        if len(a) == 1:
            if a[0] <= k:
                ans += 1
                break
            else:
                break
        min_a = min(a[0], a[-1])
        if 2 * min_a <= k:
            a[0] -= min_a
            if a[0] == 0:
                a.popleft()
                ans += 1
            a[-1] -= min_a
            if a[-1] == 0:
                a.pop()
                ans += 1
            k -= 2 * min_a
        else:
            a[0] -= (k // 2 + k % 2)
            if a[0] == 0:
                a.popleft()
                ans += 1
            a[-1] -= k // 2
            if a[-1] == 0:
                a.pop()
                ans += 1
            k -= k

    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
