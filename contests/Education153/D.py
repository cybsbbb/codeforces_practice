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
    s = insr()
    n = len(s)
    cnt1 = s.count('1')
    target = cnt1 * (n - cnt1) // 2

    dp_cur = [[10**9] * (target + 1) for i in range(cnt1 + 1)]
    dp_cur[0][0] = 0
    for i in range(n):
        dp_nxt = [[10**9] * (target + 1) for i in range(cnt1 + 1)]
        for j in range(cnt1 + 1):
            for k in range(target + 1):
                dp_nxt[j][k] = min(dp_nxt[j][k], dp_cur[j][k] + int(s[i] != '0'))
        for j in range(cnt1):
            zero_before = i - j
            if zero_before < 0:
                break
            for k in range(target + 1 - zero_before):
                dp_nxt[j + 1][k + zero_before] = min(dp_nxt[j + 1][k + zero_before],
                                                     dp_cur[j][k] + int(s[i] != '1'))
        dp_cur = dp_nxt

    print(dp_cur[-1][-1] // 2)
    return 0


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
