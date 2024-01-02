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
    n, k = inlt()
    if k % 2 == 1:
        print("No")
        return
    ans = [[0] * n for i in range(n)]
    if k % 4 == 0:
        for idx in range(k // 4):
            x, y = idx // (n // 2), idx % (n // 2)
            ans[2 * x][2 * y] = 1
            ans[2 * x + 1][2 * y] = 1
            ans[2 * x][2 * y + 1] = 1
            ans[2 * x + 1][2 * y + 1] = 1
        print("Yes")
        for i in range(n):
            print(*ans[i])
        return
    if n == 2 and k == 2:
        print("Yes")
        print("0 1")
        print("1 0")
        return
    if k == n * n - 2 or k < 6:
        print("No")
        return
    else:
        first_44 = 6 if k == 6 else 10
        requires = max(0, k - 10) // 4
        located = 0
        for idx in range((n // 2) * (n // 2)):
            if located == requires:
                break
            x, y = idx // (n // 2), idx % (n // 2)
            if x > 1 or y > 1:
                ans[2 * x][2 * y] = 1
                ans[2 * x + 1][2 * y] = 1
                ans[2 * x][2 * y + 1] = 1
                ans[2 * x + 1][2 * y + 1] = 1
                located += 1
        if first_44 == 6:
            ans[0][0] = 1
            ans[0][1] = 1
            ans[1][0] = 1
            ans[2][1] = 1
            ans[1][2] = 1
            ans[2][2] = 1
        if first_44 == 10:
            ans[0][2] = 1
            ans[0][3] = 1
            ans[1][1] = 1
            ans[1][3] = 1
            ans[2][0] = 1
            ans[2][3] = 1
            ans[3][0] = 1
            ans[3][1] = 1
            ans[3][2] = 1
            ans[3][3] = 1
        print("Yes")
        for i in range(n):
            print(*ans[i])
        return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
