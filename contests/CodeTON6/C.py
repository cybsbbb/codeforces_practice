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
    a = inlt()

    left_positions = [10**10] * (k+1)
    right_positions = [-1] * (k+1)
    for i in range(n):
        left_positions[a[i]] = min(left_positions[a[i]], i)
        right_positions[a[i]] = max(right_positions[a[i]], i)

    res = [0] * (k+1)
    cur_leftmost = 10 ** 10
    cur_rightmost = -1
    for num in range(k, 0, -1):
        if right_positions[num] == -1:
            continue
        left = left_positions[num]
        right = right_positions[num]
        cur_leftmost = min(cur_leftmost, left)
        cur_rightmost = max(cur_rightmost, right)
        res[num] = (cur_rightmost - cur_leftmost + 1) * 2

    print(*res[1:])
    return






if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
