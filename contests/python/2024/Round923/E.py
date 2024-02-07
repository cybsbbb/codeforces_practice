import bisect
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
    ans = [0] * n
    divide = n // k
    remain = n % k
    cur_start = 1
    flag = True
    for i in range(k):
        length = divide + 1 if i < remain else divide
        numbers = list(range(cur_start, cur_start + length))
        if flag is False:
            numbers = numbers[::-1]
        for idx, val in zip(range(i, n, k), numbers):
            ans[idx] = val
        flag = not flag
        cur_start += length

    print(*ans)
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
