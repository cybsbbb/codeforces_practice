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


n = inp()
ranges = []
for _ in range(n):
    ranges.append(inlt())

dp = [(0, 0)]
for i in range(n):
    pre_min, pre_max = dp[-1]
    cur_min = ranges[i][0] + pre_min
    cur_max = ranges[i][1] + pre_max
    dp.append((cur_min, cur_max))

if dp[-1][1] < 0 or dp[-1][0] > 0:
    print("No")
    exit()

ans = []

cur_val = 0
for i in range(n - 1, -1, -1):
    cur_min, cur_max = dp[i + 1]
    pre_min, pre_max = dp[i]
    val_min, val_max = ranges[i]
    if pre_min <= cur_val - val_min <= pre_max:
        ans.append(val_min)
        cur_val -= val_min
    elif pre_min <= cur_val - val_max <= pre_max:
        ans.append(val_max)
        cur_val -= val_max
    elif val_min <= cur_val - pre_min <= val_max:
        ans.append(cur_val - pre_min)
        cur_val = pre_min
    elif val_min <= cur_val - pre_max <= val_max:
        ans.append(cur_val - pre_max)
        cur_val = pre_max

print("Yes")
print(*ans[::-1])

