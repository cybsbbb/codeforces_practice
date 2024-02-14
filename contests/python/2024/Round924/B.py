import collections
import sys
import heapq

input = sys.stdin.readline

def solution():
    n = int(input())
    a = sorted(map(int, set(input().split())))
    res = 1
    right = 0
    for left in range(len(a)):
        while right < len(a) and a[right] - a[left] < n:
            right += 1
        res = max(res, right - left)

    print(res)
    return


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        solution()
