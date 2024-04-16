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
    a = [0] + inlt()
    mycow = a[k]

    ans1 = 0
    a[1], a[k] = a[k], a[1]
    for i in range(2, n + 1):
        if a[i] < mycow:
            ans1 += 1
        elif a[i] == mycow:
            continue
        else:
            break

    a[1], a[k] = a[k], a[1]
    cur_idx = 1
    while cur_idx <= n and a[cur_idx] <= mycow:
        cur_idx += 1

    if cur_idx > k:
        print(ans1)
        return

    a[k], a[cur_idx] = a[cur_idx], a[k]
    if cur_idx > 1:
        ans2 = 1
    else:
        ans2 = 0
    for i in range(cur_idx + 1, n + 1):
        if a[i] < mycow:
            ans2 += 1
        elif a[i] == mycow:
            continue
        else:
            break
    print(max(ans1, ans2))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
