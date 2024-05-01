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
    a = inlt()
    cur_xor = 0
    cnt = [0] * 32
    for i in range(n):
        cur_xor = cur_xor ^ a[i]
        for k in range(32):
            if cur_xor & (1 << k) > 0:
                cnt[k] += 1

    cnt_pre = [0] * 32

    ans = 0
    cur_xor = 0
    for i in range(n):
        cur_xor = cur_xor ^ a[i]
        cur_a = a[i]
        for k in range(32)[::-1]:
            if cur_a & (1 << k) > 0:
                ans += ((n - i) - cnt[k])
                ans += ((n - i) - cnt[k]) * (i - cnt_pre[k])
                ans += cnt[k] * cnt_pre[k]
                break
        for k in range(32):
            if cur_xor & (1 << k) > 0:
                cnt[k] -= 1
        for k in range(32):
            if cur_xor & (1 << k) > 0:
                cnt_pre[k] += 1
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
