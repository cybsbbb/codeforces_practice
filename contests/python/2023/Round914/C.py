import bisect
import collections
import sys

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
    a = inlt()
    a.sort()
    if k >= 3:
        print(0)
        return
    ans = min(a)
    for i in range(1, n):
        ans = min(ans, abs(a[i] - a[i-1]))
    if k == 1:
        print(ans)
        return
    if k == 2:
        for i in range(n):
            for j in range(i+1, n):
                tmp = abs(a[i] - a[j])
                tmp_idx = bisect.bisect_left(a, tmp)
                if tmp_idx < n:
                    ans = min(ans, abs(tmp - a[tmp_idx]))
                if tmp_idx > 0:
                    ans = min(ans, abs(tmp - a[tmp_idx - 1]))
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
