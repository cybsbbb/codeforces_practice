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
    n, m, k = inlt()
    a = inlt()
    b = inlt()
    a_set = set()
    b_set = set()

    for i in range(n):
        if 1 <= a[i] <= k:
            a_set.add(a[i])
    for j in range(m):
        if 1 <= b[j] <= k:
            b_set.add(b[j])

    if len(a_set.union(b_set)) == k and len(a_set) >= k // 2 and len(b_set) >= k // 2:
        print("YES")
    else:
        print("NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
