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


def solve():
    n, k = inlt()
    a = inlt()
    cnt = collections.Counter(a)
    keys = sorted(cnt.keys())
    keys_set = set(keys)
    cur_key = collections.deque()
    cur_v = 0
    ans = 0
    for key in keys:
        if key - 1 in keys_set:
            cur_v += cnt[key]
            cur_key.append(key)
            if len(cur_key) > k:
                left = cur_key.popleft()
                cur_v -= cnt[left]
        else:
            cur_v = cnt[key]
            cur_key = collections.deque()
            cur_key.append(key)

        ans = max(ans, cur_v)
    print(ans)
    return


t = inp()
for _ in range(t):
    solve()
