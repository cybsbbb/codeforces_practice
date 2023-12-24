import collections
import sys
import math
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
    n = inp()
    s = list(map(int, input()[:-1]))
    a = [int(x) - 1 for x in input().split()]

    indeg = [0 for i in range(n)]
    ans = []
    for x in a:
        indeg[x] += 1

    q = collections.deque()
    for i in range(n):
        if not indeg[i]:
            q.append(i)

    while q:
        i = q.popleft()
        if s[i] == 1:
            s[i] = 0
            s[a[i]] ^= 1
            ans.append(i + 1)
        indeg[a[i]] -= 1
        if not indeg[a[i]]:
            q.append(a[i])

    for i in range(n):
        if indeg[i]:
            jj = i
            ans_cur = [[], []]
            value = 0
            while True:
                indeg[jj] = 0
                value ^= s[jj]
                ans_cur[value].append(jj + 1)
                jj = a[jj]
                if jj == i:
                    break

            if value:
                print(-1)
                return

            if min(len(ans_cur[0]), len(ans_cur[1])) == 0:
                continue
            if len(ans_cur[0]) < len(ans_cur[1]):
                for x in ans_cur[0]:
                    ans.append(x)
            else:
                for x in ans_cur[1]:
                    ans.append(x)

    print(len(ans))
    print(*ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
