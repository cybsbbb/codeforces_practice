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
    s = input()[:-1]

    def helper(k):
        st = collections.deque()
        for i in range(n):
            while st and st[0] <= i - k:
                st.popleft()
            cur_val = int(s[i]) ^ 1 if len(st) % 2 == 1 else int(s[i])
            if cur_val == 0:
                if i + k > n:
                    return False
                else:
                    st.append(i)
        return True

    for i in range(1, n + 1)[::-1]:
        if helper(i):
            print(i)
            return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
