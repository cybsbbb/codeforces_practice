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
    sets = []
    for i in range(n):
        sets.append(set(inlt()[1:]))
    idx_set = set(range(n))
    cnt = collections.defaultdict(set)
    for i in range(n):
        for ele in list(sets[i]):
            cnt[ele].add(i)

    res = 0
    for ele in cnt.keys():
        sub_idx_set = cnt[ele]
        tmp = set()
        for idx in list(idx_set - sub_idx_set):
            tmp = tmp.union(sets[idx])
        res = max(res, len(tmp))

    print(res)
    return





if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
