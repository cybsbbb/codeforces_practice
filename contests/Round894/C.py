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
    left = 0
    right = n - 1
    eliminated = 0
    flag = True
    while left <= right:
        while a[right] <= eliminated:
            right -= 1
        if (a[left] - eliminated) != right - eliminated + 1:
            flag = False
            break
        eliminated += 1
        left += 1

    if flag is True:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
