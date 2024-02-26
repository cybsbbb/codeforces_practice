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
    n, q = inlt()
    c = inlt()
    for i in range(n):
        c[i] -= 1
    prefix_sum = [0]
    for i in range(n):
        prefix_sum.append(prefix_sum[-1] + c[i])
    prefix_zeros = [0]
    for i in range(n):
        prefix_zeros.append(prefix_zeros[-1] + int(c[i] == 0))

    for _ in range(q):
        l, r = inlt()
        l -= 1
        r -= 1
        if l == r:
            print("NO")
            continue
        cur_sum = prefix_sum[r + 1] - prefix_sum[l]
        cur_zeros = prefix_zeros[r + 1] - prefix_zeros[l]
        if cur_sum < cur_zeros:
            print("NO")
        else:
            print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
