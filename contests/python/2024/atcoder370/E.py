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


n, k = inlt()
a = inlt()
prefix = 0
prefix_dict = collections.defaultdict(int)
cur_tot = 1
prefix_dict[0] += 1
MOD = 998244353

ans = 1
for i in range(n):
    prefix += a[i]
    ans = cur_tot - prefix_dict[prefix - k]
    ans %= MOD
    cur_tot += ans
    cur_tot %= MOD
    prefix_dict[prefix] += ans
    prefix_dict[prefix] %= MOD

print(ans % MOD)


