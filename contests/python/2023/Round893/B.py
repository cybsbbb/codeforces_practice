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
    n, m, d = inlt()
    s = [1 - d] + inlt() + [n + 1]
    cookies = m
    for i in range(1, m + 2):
        cookies += (s[i] - s[i - 1] - 1) // d

    best_cookies = float('inf')
    best_number = -1

    for i in range(1, m + 1):
        tmp_cookies = cookies - 1 + max(0, s[i + 1] - s[i - 1] - 1) // d - max(0, s[i] - s[i - 1] - 1) // d - max(0, s[
            i + 1] - s[i] - 1) // d
        if tmp_cookies < best_cookies:
            best_cookies = tmp_cookies
            best_number = 1
        elif tmp_cookies == best_cookies:
            best_number += 1
    print(best_cookies, best_number)

    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
