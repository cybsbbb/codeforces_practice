import sys
import bisect

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
    a = inlt()
    b = inlt()
    b.sort(reverse=True)
    res = []
    a_idx = 0
    b_idx = 0
    while a_idx < n and b_idx < m:
        if a[a_idx] > b[b_idx]:
            res.append(a[a_idx])
            a_idx += 1
        else:
            res.append(b[b_idx])
            b_idx += 1
    while a_idx < n:
        res.append(a[a_idx])
        a_idx += 1
    while b_idx < m:
        res.append(b[b_idx])
        b_idx += 1

    print(*res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
