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


t = inp()
for i in range(t):
    n, q = inlt()
    a = [0] + inlt()
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        p[a[i]] = i
    q0 = [0] * q
    for i in range(q):
        l, r = inlt()
        q0[i] = (l << 40) ^ (r << 20) ^ i
    q0.sort()
    fenwick = [0] * (n + 1)
    dp = [0] * (n + 1)
    ans0 = [1] * q
    for l in range(n, 0, -1):
        i = a[l]
        dp[i] = 1
        for j in range(i, n + 1, i):
            if l <= p[j]:
                for k in range(2 * j, n + 1, j):
                    if p[j] < p[k]:
                        dp[k] += dp[j]
            if dp[j]:
                k, x = p[j], dp[j]
                while k <= n:
                    fenwick[k] += x
                    k += k & (-k)
            dp[j] = 0

        while q0 and q0[-1] >> 40 == l:
            r, i = (q0[-1] >> 20) & 0xfffff, q0.pop() & 0xfffff
            ans1 = 0
            while r > 0:
                ans1 += fenwick[r]
                r -= r & (-r)
            ans0[i] = ans1

        if not q0:
            break
    print(" ".join(map(str, ans0)))

