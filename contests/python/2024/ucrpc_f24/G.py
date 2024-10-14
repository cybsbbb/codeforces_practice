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


n, m = inlt()
males = inlt()
females = inlt()
males.sort()
females.sort()
cur_male_idx = 0
cur_female_idx = 0

ans = 0
while cur_male_idx < len(males) and (cur_female_idx + 1) < len(females):
    if males[cur_male_idx] > females[cur_female_idx + 1]:
        ans += 1
        cur_male_idx += 1
        cur_female_idx += 2
    else:
        cur_male_idx += 1
print(ans)




