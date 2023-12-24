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
    n, x = inlt()
    a = inlt()
    b = inlt()
    a_map = sorted(zip(a, range(n)))
    a.sort()
    b.sort()

    upper = 0
    a_idx = 0
    b_idx = 0
    while a_idx < n and b_idx < n:
        if a[a_idx] > b[b_idx]:
            upper += 1
            a_idx += 1
            b_idx += 1
        else:
            a_idx += 1

    lower = 0
    a_idx = 0
    b_idx = 0
    while a_idx < n and b_idx < n:
        if a[a_idx] <= b[b_idx]:
            lower += 1
            a_idx += 1
            b_idx += 1
        else:
            b_idx += 1
    lower = n - lower
    ans = [0] * n
    if lower <= x <= upper:
        res_b = b[x:] + b[:x]
        for i in range(n):
            ans[a_map[i][1]] = res_b[i]
        print("YES")
        print(*ans)
    else:
        print("NO")
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
