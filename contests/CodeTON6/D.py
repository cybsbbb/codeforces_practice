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
    c = inlt()
    k = inp()

    stack = [(-1, 0)]
    for j in range(n):
        while stack and stack[-1][1] >= c[j]:
            stack.pop()
        stack.append((j, c[j]))
    res = [0] * n

    pre_count = 10 ** 10
    for stack_i, (i, c) in enumerate(stack[1:], start=1):
        if k >= (c - stack[stack_i-1][1]):
            increments = min(pre_count, k // (c - stack[stack_i-1][1]))
            pre_count = increments
            k -= increments * (c - stack[stack_i-1][1])
            for j in range(stack[stack_i-1][0]+1, i + 1):
                res[j] = increments
        else:
            break

    print(*res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
