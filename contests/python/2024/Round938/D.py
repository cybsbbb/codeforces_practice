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


t = inp()
for i in range(t):
    n, m, k = inlt()
    a = inlt()
    b = inlt()
    counter_b = collections.Counter(sorted(b))
    counter_a = collections.Counter(sorted(a[:m]))
    ans = 0
    cur_val = sum(min(counter_a[key], counter_b[key]) for key in counter_b)
    if cur_val >= k:
        ans += 1
    for nxt_idx in range(m, n):
        head = a[nxt_idx - m]
        tail = a[nxt_idx]
        a_head = counter_a[head]
        b_head = counter_b[head]
        cur_val += min(b_head, a_head - 1) - min(b_head, a_head)
        counter_a[head] -= 1
        a_tail = counter_a[tail]
        b_tail = counter_b[tail]
        cur_val += min(b_tail, a_tail + 1) - min(b_tail, a_tail)
        counter_a[tail] += 1

        if cur_val >= k:
            ans += 1
    print(ans)
