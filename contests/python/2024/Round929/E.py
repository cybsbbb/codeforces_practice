import bisect
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
    a = inlt()
    prefix = [0]
    for ai in a:
        prefix.append(prefix[-1] + ai)
    q = inp()
    ans = []
    for _ in range(q):
        l, u = inlt()
        target = u + prefix[l - 1] + 1
        r = bisect.bisect_left(prefix, target)
        if r > n:
            ans.append(n)
            continue
        right = prefix[r] - target
        left = target - 1 - prefix[r - 1]

        if left <= right:
            r -= 1
        r = max(r, l)
        ans.append(r)

    print(*ans)
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
