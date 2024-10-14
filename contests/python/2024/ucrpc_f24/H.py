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


x, y, z = inlt()
n, k = inlt()
t = []
for _ in range(n):
    xi, yi, zi = inlt()
    ti = 100 / xi + 100 / yi + 100 / zi
    t.append(ti)
t.sort()
target_t = t[k - 1]

cur_ability = sorted([x, y, z])
cur_t = 100 / x + 100 / y + 100 / z
ans = 0
while cur_t > target_t:
    if cur_ability[0] < cur_ability[1]:
        dt = 100 / cur_ability[0] - 100 / cur_ability[1]
        if cur_t - dt >= target_t:
            ans += cur_ability[1] - cur_ability[0]
            cur_ability = sorted([cur_ability[1]] + cur_ability[1:])
        else:
            left = cur_ability[0]
            right = cur_ability[1]
            while left < right:
                mid = (left + right) // 2
                if 100 / cur_ability[0] - 100 / mid < cur_t - target_t:
                    left = mid + 1
                else:
                    right = mid
            cur_ability = sorted([left] + cur_ability[1:])
            ans += left - cur_ability[0]
    elif cur_ability[0] < cur_ability[2]:
        dt = 100 / cur_ability[0] - 100 / cur_ability[2]
        if cur_t - dt >= target_t:
            ans += cur_ability[2] - cur_ability[0]
            cur_ability = sorted([cur_ability[2]] + cur_ability[1:])
        else:
            left = cur_ability[0]
            right = cur_ability[2]
            while left < right:
                mid = (left + right) // 2
                if 100 / cur_ability[0] - 100 / mid < cur_t - target_t:
                    left = mid + 1
                else:
                    right = mid
            cur_ability = sorted([left] + cur_ability[1:])
            ans += left - cur_ability[0]
    else:
        left = cur_ability[0]
        right = 10 ** 12
        while left < right:
            mid = (left + right + 1) // 2
            if 300 / mid >= target_t:
                left = mid
            else:
                right = mid - 1
        ans += (right - cur_ability[0]) * 3
        cur_ability = sorted([right, right, right])
        cur_t = 100 / cur_ability[0] + 100 / cur_ability[1] + 100 / cur_ability[2]
        if cur_t <= target_t:
            break
        else:
            cur_ability = [right, right, right + 1]
            ans += 1

        cur_t = 100 / cur_ability[0] + 100 / cur_ability[1] + 100 / cur_ability[2]

print(ans)


