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


n, x = inlt()
weights = (list(map(float, input().split())))
weights = [int(w * 2) for w in weights]
dp_cur = dict()
dp_cur[(0, 0)] = 0
prevs = []
prev_dict = dict()

for idx, wi in enumerate(weights):
    dp_nxt = dp_cur.copy()
    prev_dict = prev_dict.copy()
    for (w1, w2), cnt in dp_cur.items():
        if w1 + wi <= x:
            if (w1 + wi, w2) not in dp_nxt:
                dp_nxt[(w1 + wi, w2)] = cnt + 1
                prev_dict[(w1 + wi, w2)] = (0, idx)
            if cnt + 1 < dp_nxt[(w1 + wi, w2)]:
                dp_nxt[(w1 + wi, w2)] = cnt + 1
                prev_dict[(w1 + wi, w2)] = (0, idx)
        if w2 + wi <= x:
            if (w1, w2 + wi) not in dp_nxt:
                dp_nxt[(w1, w2 + wi)] = cnt + 1
                prev_dict[(w1, w2 + wi)] = (1, idx)
            if cnt + 1 < dp_nxt[(w1, w2 + wi)]:
                dp_nxt[(w1, w2 + wi)] = cnt + 1
                prev_dict[(w1, w2 + wi)] = (1, idx)
    dp_cur = dp_nxt
    prevs.append(prev_dict)

if (x, x) not in dp_cur:
    print(-1)
else:
    tot = dp_cur[(x, x)]
    ans1 = []
    ans2 = []
    cur_st = (x, x)
    cur_idx = n - 1
    while cur_st != (0, 0):
        ans_idx, idx = prevs[cur_idx - 1][cur_st]
        if ans_idx == 0:
            ans1.append(idx + 1)
            cur_st = (cur_st[0] - weights[idx], cur_st[1])
        else:
            ans2.append(idx + 1)
            cur_st = (cur_st[0], cur_st[1] - weights[idx])
        cur_idx = idx

    ans1.sort()
    ans2.sort()
    print(tot)
    print(*ans1)
    print(*ans2)



