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
    s = input()[:-1]
    cur_idx = 2
    res = 0
    while cur_idx < n:
        if s[cur_idx - 2: cur_idx + 1] == 'pie':
            res += 1
            if cur_idx + 1 < n and s[cur_idx + 1] == 'e':
                cur_idx += 2
            else:
                cur_idx += 3
        elif s[cur_idx - 2: cur_idx + 1] == 'map':
            res += 1
            if cur_idx + 1 < n and s[cur_idx + 1] == 'p':
                cur_idx += 2
            else:
                cur_idx += 3
        else:
            cur_idx += 1
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
