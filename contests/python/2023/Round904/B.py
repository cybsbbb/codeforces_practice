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
    s = insr()[::-1]
    ones = s.count('1')
    res = []
    cur_target_idx = 0
    for i in range(n):
        if s[i] == '0':
            if not res:
                res.append(i - cur_target_idx)
            else:
                res.append(i - cur_target_idx + res[-1])
            cur_target_idx += 1
    for _ in range(ones):
        res.append(-1)

    print(*res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
