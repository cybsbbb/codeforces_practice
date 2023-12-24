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
    p = inlt()

    idx_1 = p.index(1)
    idx_2 = p.index(2)

    left_idx = 0
    right_idx = n-1
    min_removed = n+1

    while left_idx < right_idx:
        if p[left_idx] > p[right_idx]:
            min_removed = min(min_removed, p[left_idx])
            left_idx += 1
        else:
            min_removed = min(min_removed, p[right_idx])
            right_idx -= 1
        if left_idx == right_idx:
            print(left_idx + 1, left_idx + 1)
            return

        if min_removed - 1 == right_idx - left_idx + 1:
            if idx_2 < idx_1 and left_idx > 0:
                print(1, idx_1 - 1 + 1)
                return
            elif idx_2 > idx_1 and right_idx < n-1:
                print(n, idx_1 + 1 + 1)
                return
            elif idx_2 < idx_1 and right_idx < n-1:
                print(n, idx_1 + 1)
                return
            elif idx_2 > idx_1 and left_idx > 0:
                print(1, idx_1 + 1)
                return
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
