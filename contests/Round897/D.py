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
    b = [-1] + inlt()

    if k == 1:
        for i in range(1, n+1):
            if b[i] != i:
                print("No")
                return
        print("Yes")
        return

    seen = set()
    for i in range(1, n+1):
        if i not in seen:
            sub_seen = dict()
            sub_seen_idx = 1
            cur_idx = i
            for _ in range(n):
                sub_seen[cur_idx] = sub_seen_idx
                sub_seen_idx += 1
                seen.add(cur_idx)
                nxt_idx = b[cur_idx]
                if nxt_idx in sub_seen:
                    cycle_length = sub_seen_idx - sub_seen[nxt_idx]
                    if cycle_length != k:
                        print("No")
                        return
                    break
                if nxt_idx in seen:
                    break
                cur_idx = nxt_idx
    print("Yes")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
