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
    left = 1
    right = n - 1
    while left < n and a[left - 1] == a[left]:
        left += 1
    while right > 0 and a[right - 1] == a[right]:
        right -= 1

    left_cnt = left
    right_cnt = n - right

    if a[0] == a[-1]:
        ans = max(0, n - left_cnt - right_cnt)
    else:
        ans = n - max(left_cnt, right_cnt)
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
