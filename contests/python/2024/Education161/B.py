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
    n = inp()
    a = inlt()
    cnt = [0] * (n + 1)
    for ai in a:
        cnt[ai] += 1
    res = 0
    pre_num = 0
    for i in range(n + 1):
        value = cnt[i]
        if value >= 3:
            res += value * (value - 1) * (value - 2) // 6
        if value >= 2:
            res += value * (value - 1) // 2 * pre_num
        pre_num += value

    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
