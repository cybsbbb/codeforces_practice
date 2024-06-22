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
    st = []
    for i in range(n):
        if a[i] != -1:
            st.append(i)
    # All -1
    if len(st) == 0:
        a = [i % 2 + 1 for i in range(n)]
        print(*a)
        return

    for j in range(len(st) - 1):
        l, r = st[j], st[j + 1]
        if r - l == 1:
            if max(a[l], a[r]) // 2 != min(a[l], a[r]):
                print(-1)
                return
            else:
                continue
        left = [a[l]]
        right = [a[r]]
        while left[-1] != right[-1]:
            if left[-1] > right[-1]:
                left.append(left[-1] // 2)
            else:
                right.append(right[-1] // 2)
        if len(left) + len(right) - 1 > r - l + 1:
            print(-1)
            return
        else:
            base = left[-1]
            remaining = r - l + 1 - (len(left) + len(right) - 1)
            if remaining % 2 == 1:
                print(-1)
                return
            else:
                for _ in range(remaining // 2):
                    left.append(base * 2)
                    left.append(base)
            interval = left[:-1] + right[::-1]
            for k in range(l, r + 1):
                a[k] = interval[k - l]

    left = a[st[0]]
    for i in range(st[0]):
        if (st[0] - i) % 2 == 1:
            a[i] = 2 * left
        else:
            a[i] = left

    right = a[st[-1]]
    for i in range(st[-1] + 1, n):
        if (i - st[-1]) % 2 == 1:
            a[i] = 2 * right
        else:
            a[i] = right

    print(*a)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
