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
    n, k, x = inlt()
    a = inlt()
    a.sort(reverse=True)
    left = 0
    cur_sum = sum(a[x:]) - sum(a[:x])
    ans = cur_sum
    while left < k:
        right = left + x
        cur_sum += a[left]
        if right < n:
            cur_sum -= 2 * a[right]
        ans = max(ans, cur_sum)
        left += 1
    print(ans)
    return ans


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
