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
    a.sort()
    left_idx = 0
    right_idx = n - 1
    counter = 0
    ans = 0
    while left_idx < right_idx:
        if counter + a[left_idx] < a[right_idx]:
            counter += a[left_idx]
            ans += a[left_idx]
            left_idx += 1
        elif counter + a[left_idx] >= a[right_idx]:
            a[left_idx] -= a[right_idx] - counter
            ans += a[right_idx] - counter + 1
            right_idx -= 1
            counter = 0

    if a[left_idx] == 0:
        pass
    elif counter == 0:
        ans += min(a[left_idx], (a[left_idx] - 1) // 2 + 2)
    else:
        ans += (a[left_idx] - counter - 1) // 2 + 2

    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
