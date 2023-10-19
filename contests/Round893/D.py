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
    s = input().strip()
    ones = [0] * (n + 1)
    for i in range(n):
        ones[i+1] = ones[i] + int(s[i] == '1')

    pre = [[0] * (k + 1) for _ in range(n + 1)]
    suf = [[0] * (k + 1) for _ in range(n + 1)]

    for l in range(n):
        for r in range(l, n):
            cost = ones[r + 1] - ones[l]
            if cost > k:
                break
            pre[r + 1][cost] = max(pre[r + 1][cost], r - l + 1)
            suf[l][cost] = max(suf[l][cost], r - l + 1)

    for i in range(n+1):
        for j in range(k+1):
            if i >= 1 and j >= 1:
                pre[i][j] = max(pre[i][j], pre[i - 1][j - 1])
            if i >= 1:
                pre[i][j] = max(pre[i][j], pre[i - 1][j])
            if j >= 1:
                pre[i][j] = max(pre[i][j], pre[i][j - 1])

    for i in range(n, -1, -1):
        for j in range(k + 1):
            if i < n and j >= 1:
                suf[i][j] = max(suf[i][j], suf[i + 1][j - 1])
            if i < n:
                suf[i][j] = max(suf[i][j], suf[i + 1][j])
            if j >= 1:
                suf[i][j] = max(suf[i][j], suf[i][j - 1])

    L = [-10 ** 18] * (n + 1)
    for l in range(n + 1):
        for r in range(l, n + 1):
            cost = (r - l) - (ones[r] - ones[l])
            if cost > k:
                break
            L[r - l] = max(L[r - l], max(pre[l][k - cost], suf[r][k - cost]))
    ans = []
    for i in range(1, n + 1):
        mx = max(i * L[l1] + l1 for l1 in range(n + 1))
        ans.append(mx)
    print(*ans)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
