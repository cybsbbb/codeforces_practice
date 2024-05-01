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


t = inp()
for i in range(t):
    n, k = inlt()
    ans = []
    left_one = 32
    while (1 << left_one) & k == 0:
        left_one -= 1
    for i in range(left_one):
        ans.append(1 << i)
    for i in range(left_one + 1, 20):
        if (1 << i) <= n:
            ans.append(1 << i)
    if k & ((1 << left_one) - 1) > 0:
        ans.append(k & ((1 << left_one) - 1))
    ans.append(k + 1)
    ans.append(k | 1 << (left_one + 1))

    print(len(ans))
    print(*ans)

