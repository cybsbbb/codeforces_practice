import collections
import sys
import heapq
import math

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


N = 10 ** 6 + 1
primes = []
min_div = list(range(N))
for i in range(2, N):
    if min_div[i] == i:
        primes.append(i)
    for j in primes:
        if i * j >= N or min_div[i] < j:
            break
        min_div[i * j] = j


def solution():
    n, k = inlt()
    a = inlt()

    parent = [i for i in range(2 * n - 1)]
    def find(x):
        x_copy = x
        while x != parent[x]:
            x = parent[x]
        while x_copy != x:
            parent[x_copy], x_copy = x, parent[x_copy]
        return x
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[a] = b

    ans = sum(x == 1 for x in a) * (n - 2) + int(a[0] == 1)
    p_pos = {}

    for i in range(n):
        while a[i] != 1:
            p = min_div[a[i]]
            if p not in p_pos:
                p_pos[p] = [i, i]
            else:
                if i - p_pos[p][1] <= k:
                    union(i, p_pos[p][1])
                    if p_pos[p][1] != 0:
                        union(i - n, p_pos[p][1] - n)
                p_pos[p][1] = i
            while a[i] % p == 0:
                a[i] //= p

    for l, r in p_pos.values():
        if r != 0 and l - (r - n) <= k:
            union(l, r - n)

    ans += sum(parent[i] == i for i in range(len(parent)))
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()

