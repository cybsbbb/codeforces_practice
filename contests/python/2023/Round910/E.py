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
    s = insr()
    t = insr()
    chr_index = {c: collections.deque() for c in 'abcdefghijklmnopqrstuvwxyz'}
    for i in range(n):
        chr_index[s[i]].append(i)
    for c in t:
        if not chr_index[c]:
            print("NO")
            return
        nxt_index = chr_index[c].popleft()
        for i in range(ord(c) - ord('a')):
            pre_chr = chr(i + ord('a'))
            while chr_index[pre_chr] and chr_index[pre_chr][0] < nxt_index:
                chr_index[pre_chr].popleft()
    print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
