import sys
import heapq
import collections

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
    n, q = inlt()
    a = inlt()
    dp = [[0] * 60 for i in range(n)]

    for k in range(60):
        for i in range(n):
            if not (a[i] >> k) & 1:
                dp[i][k] += (1 << k) - (a[i] & ((1 << (k+1)) - 1))

    for _ in range(q):
        flag = [False] * n
        ki = inp()
        ans = 0

        for k in range(60)[::-1]:
            tmp = 0
            for i in range(n):
                if flag[i] is True:
                    tmp += (1 << k)
                else:
                    tmp += dp[i][k]
                if tmp > ki:
                    break
            if tmp <= ki:
                ki -= tmp
                ans += (1 << k)
                for i in range(n):
                    if dp[i][k] != 0:
                        flag[i] = True
        print(ans)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
