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
    b = inlt()
    c = inlt()
    a_sorted_idx = sorted(list(range(n)), key=lambda i: a[i], reverse=True)
    b_sorted_idx = sorted(list(range(n)), key=lambda i: b[i], reverse=True)
    c_sorted_idx = sorted(list(range(n)), key=lambda i: c[i], reverse=True)

    ans = 0
    for i in range(3):
        a_day = a_sorted_idx[i]
        for j in range(3):
            b_day = b_sorted_idx[j]
            if a_day == b_day:
                continue
            for k in range(3):
                c_day = c_sorted_idx[k]
                if a_day == c_day or b_day == c_day:
                    continue
                ans = max(ans, a[a_day] + b[b_day] + c[c_day])
    print(ans)
    return ans


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
