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
    s = insr()
    pos = inp()
    n = len(s)
    if pos <= n:
        print(s[pos-1], end='')
        return
    stack = []
    cur_idx = 0
    cur_length = n
    removed = 0
    for i in range(n):
        while cur_idx < n and (not stack or stack[-1] <= s[cur_idx]):
            stack.append(s[cur_idx])
            cur_idx += 1
        stack.pop()
        removed += 1
        if (pos - cur_length) <= (n - removed):
            if (pos - cur_length) <= len(stack):
                print(stack[pos - cur_length - 1], end='')
                return
            else:
                print(s[cur_idx + pos - cur_length - len(stack) - 1], end='')
                return
        cur_length += (n - removed)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
