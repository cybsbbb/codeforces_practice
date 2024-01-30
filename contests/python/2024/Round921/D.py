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
    n, m, k = inlt()
    MOD = 10 ** 9 + 7
    tot_f = 0
    for _ in range(m):
        ai, bi, fi = inlt()
        tot_f += fi

    all_pairs = n * (n - 1) // 2
    denominator = pow(all_pairs, 2, MOD)
    denominator = pow(denominator, MOD - 2, MOD)

    numerator = all_pairs * tot_f * k
    numerator += m * k * (k - 1) // 2

    ans = (numerator * denominator) % MOD
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
