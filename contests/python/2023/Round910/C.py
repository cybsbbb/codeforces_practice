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
    if k < (m - 1) + (n - 1):
        print("NO")
        return
    if (k - (m - 1) - (n - 1)) % 2 != 0:
        print("NO")
        return

    print("YES")
    ans_1 = [['B']*(m-1) for i in range(n)]
    ans_2 = [['B']*(m) for i in range(n-1)]

    ans_1[0][0] = 'R'
    ans_1[1][0] = 'R'
    for i in range(1, m-1):
        if ans_1[0][i - 1] == 'B':
            ans_1[0][i] = 'R'
        else:
            ans_1[0][i] = 'B'
    if ans_1[0][-1] == 'R':
        ans_2[0][-1] = 'B'
    else:
        ans_2[0][-1] = 'R'

    for j in range(1, n-1):
        if ans_2[j - 1][-1] == 'B':
            ans_2[j][-1] = 'R'
        else:
            ans_2[j][-1] = 'B'

    if ans_2[-2][-1] == 'B':
        ans_1[-2][-1] = 'R'
        ans_2[-1][-2] = 'B'
        ans_1[-1][-1] = 'R'
    else:
        ans_1[-2][-1] = 'B'
        ans_2[-1][-2] = 'R'
        ans_1[-1][-1] = 'B'

    for i in range(n):
        print(*ans_1[i])
    for j in range(n-1):
        print(*ans_2[j])

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
