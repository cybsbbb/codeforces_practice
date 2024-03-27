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
    n, k = inlt()
    MOD = 10 ** 9 + 7
    a = inlt()
    sum_a = 0
    for ai in a:
        sum_a = (sum_a + ai) % MOD
    max_continues_val = 0
    cur_val = 0
    for ai in a:
        cur_val += ai
        if cur_val < 0:
            cur_val = 0
        max_continues_val = max(max_continues_val, cur_val)

    if max_continues_val == 0:
        print(sum_a)
    else:
        sum_a += (pow(2, k, MOD) - 1) * max_continues_val
        sum_a %= MOD
        print(sum_a)
