
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
    c = inlt()
    start_color = c[0]
    end_color = c[-1]
    cnt_start = 0
    start_idx = 0
    while start_idx < n and cnt_start < k:
        if c[start_idx] == start_color:
            cnt_start += 1
        start_idx += 1
    if cnt_start < k:
        print('NO')
        return
    cnt_end = 0
    end_idx = n-1
    while end_idx >= 0 and cnt_end < k:
        if c[end_idx] == end_color:
            cnt_end += 1
        end_idx -= 1
    if cnt_end < k:
        print('NO')
        return

    if start_color != end_color and end_idx + 1 < start_idx - 1:
        print("NO")
        return

    print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
