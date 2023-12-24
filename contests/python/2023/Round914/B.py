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
    a = inlt()
    a_sorted = sorted(zip(a, range(n)))
    ans = [0] * n
    cur_sum = a_sorted[0][0]
    pre_idx = 0
    for i in range(1, n):
        if a_sorted[i][0] > cur_sum:
            for j in range(pre_idx, i):
                ans[a_sorted[j][1]] = i - 1
            pre_idx = i
        cur_sum += a_sorted[i][0]
    for j in range(pre_idx, n):
        ans[a_sorted[j][1]] = n - 1

    print(*ans)
    return




if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
