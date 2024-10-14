import collections
import sys
import heapq
import math

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
    s0 = input()[:-1]
    s1 = input()[:-1]
    s = [s0, s1]
    dp = dict()
    dp[(0, 0)] = 0
    for i in range(2 * n // 3):
        dp_nxt = dict()
        for (i0, i1), cnt in dp.items():
            if i0 == i1:
                # --
                # -
                if i0 + 2 <= n and i1 + 1 <= n:
                    vote = int((s[0][i0: i0 + 2] + s[1][i1: i1 + 1]).count('A') >= 2)
                    if (i0 + 2, i1 + 1) not in dp_nxt:
                        dp_nxt[(i0 + 2, i1 + 1)] = cnt + vote
                    else:
                        dp_nxt[(i0 + 2, i1 + 1)] = max(dp_nxt[(i0 + 2, i1 + 1)], cnt + vote)
                # -
                # --
                if i0 + 1 <= n and i1 + 2 <= n:
                    vote = int((s[0][i0: i0 + 1] + s[1][i1: i1 + 2]).count('A') >= 2)
                    if (i0 + 1, i1 + 2) not in dp_nxt:
                        dp_nxt[(i0 + 1, i1 + 2)] = cnt + vote
                    else:
                        dp_nxt[(i0 + 1, i1 + 2)] = max(dp_nxt[(i0 + 1, i1 + 2)], cnt + vote)
                # ---
                #
                if i0 + 3 <= n:
                    vote = int((s[0][i0: i0 + 3]).count('A') >= 2)
                    if (i0 + 3, i1) not in dp_nxt:
                        dp_nxt[(i0 + 3, i1)] = cnt + vote
                    else:
                        dp_nxt[(i0 + 3, i1)] = max(dp_nxt[(i0 + 3, i1)], cnt + vote)
                #
                # ---
                if i1 + 3 <= n:
                    vote = int((s[1][i1: i1 + 3]).count('A') >= 2)
                    if (i0, i1 + 3) not in dp_nxt:
                        dp_nxt[(i0, i1 + 3)] = cnt + vote
                    else:
                        dp_nxt[(i0, i1 + 3)] = max(dp_nxt[(i0, i1 + 3)], cnt + vote)
            elif i0 < i1:
                if i1 - i0 == 1:
                    if i0 + 2 <= n and i1 + 1 <= n:
                        vote = int((s[0][i0: i0 + 2] + s[1][i1: i1 + 1]).count('A') >= 2)
                        if (i0 + 2, i1 + 1) not in dp_nxt:
                            dp_nxt[(i0 + 2, i1 + 1)] = cnt + vote
                        else:
                            dp_nxt[(i0 + 2, i1 + 1)] = max(dp_nxt[(i0 + 2, i1 + 1)], cnt + vote)
                if i0 + 3 <= n:
                    vote = int((s[0][i0: i0 + 3]).count('A') >= 2)
                    if (i0 + 3, i1) not in dp_nxt:
                        dp_nxt[(i0 + 3, i1)] = cnt + vote
                    else:
                        dp_nxt[(i0 + 3, i1)] = max(dp_nxt[(i0 + 3, i1)], cnt + vote)
            else:
                if i0 - i1 == 1:
                    if i0 + 1 <= n and i1 + 2 <= n:
                        vote = int((s[0][i0: i0 + 1] + s[1][i1: i1 + 2]).count('A') >= 2)
                        if (i0 + 1, i1 + 2) not in dp_nxt:
                            dp_nxt[(i0 + 1, i1 + 2)] = cnt + vote
                        else:
                            dp_nxt[(i0 + 1, i1 + 2)] = max(dp_nxt[(i0 + 1, i1 + 2)], cnt + vote)
                if i1 + 3 <= n:
                    vote = int((s[1][i1: i1 + 3]).count('A') >= 2)
                    if (i0, i1 + 3) not in dp_nxt:
                        dp_nxt[(i0, i1 + 3)] = cnt + vote
                    else:
                        dp_nxt[(i0, i1 + 3)] = max(dp_nxt[(i0, i1 + 3)], cnt + vote)
        dp = dp_nxt

    print(dp[(n, n)])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
