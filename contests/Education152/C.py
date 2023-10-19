
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
    n, m = inlt()
    s = input()[:-1]
    operations = []
    for i in range(m):
        operations.append(inlt())

    pre_zero_idx = [-1] * n
    pre_idx = -1
    for i in range(n):
        if s[i] == '0':
            pre_idx = i
        pre_zero_idx[i] = pre_idx

    back_one_idx = [-1] * n
    pre_idx = n
    for i in range(n-1, -1, -1):
        if s[i] == '1':
            pre_idx = i
        back_one_idx[i] = pre_idx

    res = set()
    for x, y in operations:
        x -= 1
        y -= 1
        if pre_zero_idx[y] < back_one_idx[x]:
            res.add((-1, -1))
        else:
            res.add((back_one_idx[x], pre_zero_idx[y]))
    print(len(res))


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
