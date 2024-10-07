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


n, k = inlt()
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    ai, bi = inlt()
    ai -= 1
    bi -= 1
    tree[ai].append(bi)
    tree[bi].append(ai)
v = inlt()
m = len(v)
v_set = set()
for vi in v:
    v_set.add(vi - 1)
cnt = [0] * n
ans = n

st = [(0, -1, False)]
while st:
    cur, par, flag = st.pop()
    if flag is False:
        st.append((cur, par, True))
        for nxt in tree[cur]:
            if nxt == par:
                continue
            st.append((nxt, cur, False))
    else:
        child_list = []
        res = 1 if cur in v_set else 0
        for nxt in tree[cur]:
            if nxt == par:
                continue
            if cnt[nxt] != 0:
                child_list.append(cnt[nxt])
            res += cnt[nxt]
        cnt[cur] = res
        if res < m:
            child_list.append(m - res)

        if cur not in v_set and len(child_list) == 1:
            ans -= 1

print(ans)
