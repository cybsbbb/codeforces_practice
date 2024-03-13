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
    n, m, x = inlt()
    cur_state = [False] * n
    cur_state[x - 1] = True
    nxt_state = [False] * n
    for _ in range(m):
        ri, ci = input()[:-1].split()
        ri = int(ri)
        for i in range(n):
            nxt_state[i] = False
        if ci == '?':
            for i in range(n):
                if cur_state[i]:
                    nxt_state[(i + ri) % n] = True
                    nxt_state[(i - ri) % n] = True
        elif ci == '0':
            for i in range(n):
                if cur_state[i]:
                    nxt_state[(i + ri) % n] = True
        else:
            for i in range(n):
                if cur_state[i]:
                    nxt_state[(i - ri) % n] = True
        cur_state, nxt_state = nxt_state, cur_state

    res = []
    for i in range(n):
        if cur_state[i]:
            res.append(i + 1)
    print(len(res))
    print(*res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
