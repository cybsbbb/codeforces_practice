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
    n, m = inlt()
    a = inlt()
    s = insr()
    st = []
    left = 0
    right = n - 1
    for i in range(n):
        if s[i] == 'L':
            st.append(a[left])
            left += 1
        else:
            st.append(a[right])
            right -= 1
    res = []
    cur_val = 1
    while st:
        cur_val = (cur_val * st.pop()) % m
        res.append(cur_val)

    print(*res[::-1])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
