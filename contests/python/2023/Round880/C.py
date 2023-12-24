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
    A, B, C, k = inlt()
    if max(A, B) + 1 < C:
        print(-1)
        return

    min_A = 10 ** (A - 1)
    max_A = 10 ** A - 1
    min_B = 10 ** (B - 1)
    max_B = 10 ** B - 1
    min_C = 10 ** (C - 1)
    max_C = 10 ** C - 1

    A_start = max(min_A, min_C - max_B)

    while A_start <= max_A:
        B_left = max(min_B, min_C - A_start)
        B_right = min(max_B, max_C - A_start)
        B_cnt = B_right - B_left + 1
        if B_cnt <= 0:
            break
        if k > B_cnt:
            k -= B_cnt
        else:
            print(f"{A_start} + {B_left + k - 1} = {A_start + B_left + k - 1}")
            return
        A_start += 1

    print(-1)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
