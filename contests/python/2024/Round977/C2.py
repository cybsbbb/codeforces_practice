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
    n, m, q = inlt()
    a = inlt()
    a_idx = dict()
    for i, ai in enumerate(a):
        a_idx[ai] = i
    b = inlt()
    member_idxs = [[] for _ in range(n)]
    first = [m + 1] * n
    for i, bi in enumerate(b):
        first[a_idx[bi]] = min(first[a_idx[bi]], i)
        member_idxs[a_idx[bi]].append(i)

    valid = 0
    for i in range(1, n):
        if first[i] >= first[i - 1]:
            valid += 1

    if valid == n - 1:
        print("YA")
    else:
        print("TIDAK")

    for _ in range(q):
        si, ti = inlt()
        si -= 1
        cur_member = b[si]
        cur_member_idx = a_idx[cur_member]

        b[si] = -1
        if first[cur_member_idx] == si:
            while member_idxs[cur_member_idx] and b[member_idxs[cur_member_idx][0]] != cur_member:
                heapq.heappop(member_idxs[cur_member_idx])
            nxt_first = member_idxs[cur_member_idx][0] if member_idxs[cur_member_idx] else m + 1
            if cur_member_idx > 0 and first[cur_member_idx] >= first[cur_member_idx - 1]:
                valid -= 1
            if cur_member_idx < n - 1 and first[cur_member_idx + 1] >= first[cur_member_idx]:
                valid -= 1
            first[cur_member_idx] = nxt_first
            if cur_member_idx > 0 and first[cur_member_idx] >= first[cur_member_idx - 1]:
                valid += 1
            if cur_member_idx < n - 1 and first[cur_member_idx + 1] >= first[cur_member_idx]:
                valid += 1

        b[si] = ti
        cur_member = ti
        cur_member_idx = a_idx[ti]
        heapq.heappush(member_idxs[cur_member_idx], si)
        if first[cur_member_idx] > si:
            while member_idxs[cur_member_idx] and b[member_idxs[cur_member_idx][0]] != cur_member:
                heapq.heappop(member_idxs[cur_member_idx])
            nxt_first = member_idxs[cur_member_idx][0] if member_idxs[cur_member_idx] else m + 1
            if cur_member_idx > 0 and first[cur_member_idx] >= first[cur_member_idx - 1]:
                valid -= 1
            if cur_member_idx < n - 1 and first[cur_member_idx + 1] >= first[cur_member_idx]:
                valid -= 1
            first[cur_member_idx] = nxt_first
            if cur_member_idx > 0 and first[cur_member_idx] >= first[cur_member_idx - 1]:
                valid += 1
            if cur_member_idx < n - 1 and first[cur_member_idx + 1] >= first[cur_member_idx]:
                valid += 1

        if valid == n - 1:
            print("YA")
        else:
            print("TIDAK")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
