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
    a = [0] * (n + 1)
    c = [0] * (n + 1)
    cur_group = 1
    cur_idx = 1
    while cur_idx <= n:
        cur_len = min(k, n - cur_idx + 1)
        for i in range(cur_idx, cur_idx + cur_len):
            c[i] = cur_group
        cur_group += 1
        a[cur_idx: cur_idx + cur_len] = [i + cur_idx for i in range(cur_len // 2)[::-1]] + [i + cur_idx for i in range(cur_len // 2, cur_len)[::-1]]
        cur_idx += cur_len

    print(*a[1:])
    print(c[-1])
    print(*c[1:])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
