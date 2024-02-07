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
    diff_index = []
    for i in range(n-1):
        if a[i+1] != a[i]:
            diff_index.append(i)

    q = inp()
    for i in range(q):
        l, r = inlt()
        l -= 1
        r -= 1
        check_idx = bisect.bisect_left(diff_index, l)
        if check_idx < len(diff_index) and diff_index[check_idx] < r:
            print(diff_index[check_idx] + 1, diff_index[check_idx] + 2)
        else:
            print(-1, -1)

    print()
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
