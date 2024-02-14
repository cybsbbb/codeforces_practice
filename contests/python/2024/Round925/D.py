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
    n, x, y = inlt()
    a = inlt()
    cnt = collections.defaultdict(int)

    ans = 0
    for i in range(n):
        ai = a[i]
        ans += cnt[((x - ai % x) % x, ai % y)]
        cnt[(ai % x, ai % y)] += 1

    print(ans)
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
