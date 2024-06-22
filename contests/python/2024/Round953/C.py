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
    n, k = inlt()
    limitation = 0
    for i in range(n - 1, 0, -2):
        limitation += i * 2
    if k > limitation or k % 2 == 1:
        print("No")
        return
    ans = list(range(1, n + 1))
    left = 0
    right = n - 1
    while k > 0:
        if 2 * abs(ans[left] - ans[right]) > k:
            left += 1
        else:
            ans[left], ans[right] = ans[right], ans[left]
            k -= 2 * abs(ans[left] - ans[right])
            left += 1
            right -= 1
    print("YES")
    print(*ans)
    return





if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





