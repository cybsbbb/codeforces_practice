import math
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
    n, q = inlt()
    a = inlt()

    limit = int(math.sqrt(n))

    prefix1 = [[0] * n for _ in range(limit + 1)]
    prefix2 = [[0] * n for _ in range(limit + 1)]

    for t in range(1, limit + 1):
        for i in range(n):
            cur_n = i // t + 1
            prefix1[t][i] = prefix1[t][i - t] + a[i]
            prefix2[t][i] = prefix2[t][i - t] + a[i] * cur_n

    res = []
    for _ in range(q):
        s, d, k = inlt()
        s -= 1
        if d >= limit:
            ans = sum(a[s + i * d] * (i + 1) for i in range(k))
            res.append(ans)
            continue
        else:
            ans = prefix2[d][s + d * (k - 1)]
            if (s - d) >= 0:
                ans -= prefix2[d][s - d]
                cur_n = s // d
                ans -= cur_n * (prefix1[d][s + d * (k - 1)] - prefix1[d][s - d])
            res.append(ans)
            continue

    print(*res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
