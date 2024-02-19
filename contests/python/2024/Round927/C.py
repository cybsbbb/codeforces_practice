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
    a = collections.deque(inlt())
    s = insr()
    st = []
    for c in s:
        if c == 'L':
            st.append(a.popleft())
        else:
            st.append(a.pop())
    res = 1
    ans = []
    while st:
        res = res * st.pop() % m
        ans.append(res)

    print(*ans[::-1])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
