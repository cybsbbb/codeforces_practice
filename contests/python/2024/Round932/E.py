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
    n = inp()
    courses = []
    for i in range(n):
        courses.append(inlt())
    q = inp()
    must = [[0] * (n + 1) for _ in range(30)]
    bits = [[0] * (n + 1) for _ in range(30)]
    for i in range(n):
        for j in range(30)[::-1]:
            if (courses[i][0] >> j) & 1 == (courses[i][1] >> j) & 1:
                must[j][i + 1] = must[j][i] + ((courses[i][0] >> j) & 1)
                bits[j][i + 1] = bits[j][i]
            else:
                for k in range(j, -1, -1):
                    bits[k][i + 1] = bits[k][i] + ((courses[i][1] >> k) & 1)
                    must[k][i + 1] = must[k][i]
                break

    res = []
    for _ in range(q):
        l, r = inlt()
        ans = 0
        for i in range(30)[::-1]:
            if must[i][r] - must[i][l - 1]:
                ans += (1 << i)
        for i in range(30)[::-1]:
            if ans & (1 << i):
                if bits[i][r] - bits[i][l - 1] > 0:
                    ans |= ((1 << i) - 1)
                    break
            else:
                if bits[i][r] - bits[i][l - 1] >= 2:
                    ans |= ((1 << (i + 1)) - 1)
                elif bits[i][r] - bits[i][l - 1] > 0:
                    ans |= (1 << i)
        res.append(ans)

    print(*res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()

