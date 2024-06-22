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
    s = input()[:-1]
    n = len(s)
    stat = collections.defaultdict(int)
    key_heap = []
    ans = 0
    cur_val = 0
    for c in s:
        if c == '(':
            cur_val += 1
        else:
            cur_val -= 1
        threshold = (cur_val + 1) // 2 - 1
        while key_heap and key_heap[0] <= threshold:
            drop_key = heapq.heappop(key_heap)
            del stat[drop_key]
        if cur_val not in stat:
            heapq.heappush(key_heap, cur_val)
        ans += stat[cur_val]
        stat[cur_val] += 1

    print(ans)
    return






t = inp()
for _ in range(t):
    solve()
