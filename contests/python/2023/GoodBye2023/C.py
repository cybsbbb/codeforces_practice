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


def solution():
    n = inp()
    a = inlt()
    ans = []
    ans.append(a[0])
    odd = 0
    prefix_sum = a[0]
    if a[0] % 2 == 1:
        odd += 1
    for i in range(1, n):
        ai = a[i]
        prefix_sum += ai
        if ai % 2 == 1:
            odd += 1
        tmp_ans = prefix_sum
        tmp_ans -= odd // 3
        if odd % 3 == 1:
            tmp_ans -= 1
        ans.append(tmp_ans)
    print(*ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
