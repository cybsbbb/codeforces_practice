import collections
import math
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


candidate = [[] for i in range(20)]

for n in range(1, 20):
    for switch in range(1, 1 << n):
        s = bin(switch)[2:]
        s = (n - len(s)) * '0' + s

        light = [0] * (n + 1)
        for i in range(n):
            if s[i] == '1':
                for j in range(i+1, n+1, i+1):
                    light[j] ^= 1
        if sum(light) <= n // 5:
            candidate[n].append(s)


def solution():
    n, m = inlt()
    pairs = []
    for i in range(m):
        pairs.append(inlt())

    if n >= 20:
        print(n)
        print(*range(1, n + 1))
        return

    for s in candidate[n]:
        flag = True
        for u, v in pairs:
            if s[u-1] == '1' and s[v-1] == '0':
                flag = False
                break
        if flag:
            ans = [i + 1 for i in range(n) if s[i] == '1']
            print(len(ans))
            print(*ans)
            return
    print(-1)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
