from collections import deque
import sys

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
intervals = []
for _ in range(n):
    s, t = inlt()
    intervals.append((s, 1))
    intervals.append((s + t, - 1))

intervals.sort()
m = len(intervals)

res = [0] * n

pre_cnt = 0
pre_loc = 0
cur_idx = 0

while cur_idx < m:
    cur_loc = intervals[cur_idx][0]
    if pre_cnt > 0:
        res[pre_cnt - 1] += (cur_loc - pre_loc)
    cur_cnt = pre_cnt
    while cur_idx < m and intervals[cur_idx][0] == cur_loc:
        cur_cnt += intervals[cur_idx][1]
        cur_idx += 1
    pre_cnt = cur_cnt
    pre_loc = cur_loc

print(*res)




