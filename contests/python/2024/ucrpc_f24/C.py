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


n = inp()
stat = dict()
for _ in range(n):
    g, s, b = input().split()
    if g not in stat:
        stat[g] = [0] * 3
    if s not in stat:
        stat[s] = [0] * 3
    if b not in stat:
        stat[b] = [0] * 3
    stat[g][0] += 1
    stat[s][1] += 1
    stat[b][2] += 1

rank = []
for key, (gi, si, bi) in stat.items():
    tot = gi + si + bi
    rank.append((-tot, -gi, -si, -bi, key))
rank.sort()

print(rank[0][4], -rank[0][1], -rank[0][2], -rank[0][3])
print(rank[1][4], -rank[1][1], -rank[1][2], -rank[1][3])
print(rank[2][4], -rank[2][1], -rank[2][2], -rank[2][3])

