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


MOD = 998244353

t = 1
for _ in range(t):
    n = inp()
    a = inlt()
    a.sort()

    dp = [0] * 5001
    dp[0] = 1

    out_odd = 0
    out_odd_cnt = 0
    out_even = 0
    out_even_cnt = 0

    ans = 0
    for ai in a:
        ans += sum(dp[:ai + 1]) * ai
        ans %= MOD
        for v in range(ai + 1, 5001):
            if dp[v] > 0:
                ans += dp[v] * ((v + ai + 1) // 2)
                ans %= MOD
        if ai % 2 == 1:
            ans += (ai * out_odd_cnt + out_odd) // 2
            ans %= MOD
            ans += (ai * out_even_cnt + out_even + out_even_cnt) // 2
            ans %= MOD
        else:
            ans += (ai * out_odd_cnt + out_odd + out_odd_cnt) // 2
            ans %= MOD
            ans += (ai * out_even_cnt + out_even) // 2
            ans %= MOD

        for v in range(5001)[::-1]:
            nxt_v = v + ai
            nxt_v_cnt = dp[v]
            if nxt_v > 5000:
                if nxt_v % 2 == 1:
                    out_odd += nxt_v * nxt_v_cnt
                    out_odd %= MOD
                    out_odd_cnt += nxt_v_cnt
                    out_odd_cnt %= MOD
                else:
                    out_even += nxt_v * nxt_v_cnt
                    out_even %= MOD
                    out_even_cnt += nxt_v_cnt
                    out_even_cnt %= MOD
            else:
                dp[nxt_v] += nxt_v_cnt
                dp[nxt_v] %= MOD

    print(ans % MOD)
    exit()
