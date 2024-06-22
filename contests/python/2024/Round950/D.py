import collections
import sys
import heapq
import math

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
    forward = [-1] * n
    backward = [-1] * n
    forward[0] = 1
    backward[-1] = a[-1]
    for i in range(1, n):
        cur_gcd = math.gcd(a[i], a[i - 1])
        if cur_gcd >= forward[i - 1]:
            forward[i] = cur_gcd
        else:
            break
    for i in range(1, n)[::-1]:
        cur_gcd = math.gcd(a[i], a[i - 1])
        if cur_gcd <= backward[i]:
            backward[i - 1] = cur_gcd
        else:
            break
    if backward[1] > 0 or backward[0] > 0 or forward[-1] > 0 or forward[-2] > 0:
        print("YES")
        return
    else:
        ans = False
        for i in range(1, n - 1):
            left = forward[i - 1]
            mid = math.gcd(a[i - 1], a[i + 1])
            right = backward[i + 1]
            if left > 0 and right > 0 and (left <= mid <= right):
                ans = True

        print("YES" if ans else "NO")
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





