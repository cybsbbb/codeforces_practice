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
    b = inlt()
    cur_idx = n - 1
    seen = set()
    seen.add(cur_idx)
    for _ in range(k):
        if b[cur_idx] > n:
            print("No")
            return
        else:
            cur_idx = (cur_idx - b[cur_idx] + n) % n
            if cur_idx in seen:
                break
            seen.add(cur_idx)

    print("Yes")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
