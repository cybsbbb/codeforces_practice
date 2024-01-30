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
    b = inlt()
    ans = sorted(zip(a, b))
    a_ans = [ans[i][0] for i in range(n)]
    b_ans = [ans[i][1] for i in range(n)]
    print(*a_ans)
    print(*b_ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
