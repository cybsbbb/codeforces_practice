import collections
import sys
import heapq
import math
import bisect

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
    ss = []
    for _ in range(n):
        ss.append(input()[:-1])
    letter = ['n', 'a', 'r', 'e', 'k']
    letter_set = set(letter)
    # letter_idx = {'n': 0, 'a': 1, 'r': 2, 'e': 3, 'k': 4}
    dp_cur = [0, -10**18, -10**18, -10**18, -10**18]
    for i in range(n):
        s = ss[i]
        dp_nxt = dp_cur[:]
        for start in range(5):
            cur_val = dp_cur[start]
            cur_idx = start
            for c in s:
                if c == letter[cur_idx]:
                    cur_idx = (cur_idx + 1) % 5
                    if cur_idx == 0:
                        cur_val += 5
                elif c in letter_set:
                    cur_val -= 1
            dp_nxt[cur_idx] = max(dp_nxt[cur_idx], cur_val)
        dp_cur = dp_nxt
    ans = 0
    for i in range(5):
        ans = max(ans, dp_cur[i] - i)
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





