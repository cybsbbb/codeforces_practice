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
    a = collections.deque(inlt())
    ans = 0
    while a and k > 0:
        if len(a) == 1:
            if a[0] > k:
                break
            else:
                ans += 1
                break
        if k >= min(a[0], a[-1]) * 2:
            tmp = min(a[0], a[-1])
            k -= 2 * tmp
            a[0] -= tmp
            if a[0] == 0:
                ans += 1
                a.popleft()
            a[-1] -= tmp
            if a[-1] == 0:
                ans += 1
                a.pop()
        else:
            tmp1 = k // 2
            tmp2 = k % 2
            k = 0
            a[0] -= tmp1 + tmp2
            if a[0] == 0:
                ans += 1
                a.popleft()
            a[-1] -= tmp1
            if a[-1] == 0:
                ans += 1
                a.pop()

    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
