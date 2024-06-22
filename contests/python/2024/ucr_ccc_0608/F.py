import collections
import sys
import heapq
import math
from functools import cache

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


def transfer(c):
    if c.islower():
        return c.upper()
    else:
        return c.lower()


def solution():
    s = input()[:-1]
    n = len(s)
    pare_match = dict()
    st = []
    for i in range(n):
        if s[i] == '(':
            st.append(i)
        elif s[i] == ')':
            match = st.pop()
            pare_match[i] = match
            pare_match[match] = i

    cur_direction = 1
    cur_idx = 0
    st = []
    ans = []
    while cur_idx < n:
        if s[cur_idx] != '(' and s[cur_idx] != ')':
            if len(st) % 2 == 0:
                ans.append(s[cur_idx])
            else:
                ans.append(transfer(s[cur_idx]))
            cur_idx += cur_direction
        else:
            if st and st[-1] == cur_idx:
                idx = st.pop()
                cur_direction *= -1
                cur_idx = pare_match[idx] + cur_direction
            else:
                st.append(cur_idx)
                cur_direction *= -1
                cur_idx = pare_match[cur_idx] + cur_direction

    print(''.join(ans))
    return



if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()





