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
    n, m, k = inlt()
    a = inlt()
    b = inlt()
    cnt_b = collections.Counter(sorted(b))
    cnt_a = collections.Counter(sorted(a[:m]))
    ans = 0
    cur_val = sum(min(cnt_a[key], cnt_b[key]) for key in cnt_b)
    if cur_val >= k:
        ans += 1
    for i in range(n - m):
        head = a[i + m]
        tail = a[i]
        a_head = cnt_a[head]
        b_head = cnt_b[head]
        cur_val += min(a_head + 1, b_head) - min(a_head, b_head)
        cnt_a[head] += 1
        a_tail = cnt_a[tail]
        b_tail = cnt_b[tail]
        cur_val += min(a_tail - 1, b_tail) - min(a_tail, b_tail)
        cnt_a[tail] -= 1
        if cur_val >= k:
            ans += 1
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
