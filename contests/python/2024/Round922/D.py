import bisect
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


t = inp()
for i in range(t):
    n = inp()
    a = inlt()
    prefix = [0]
    for i in range(n):
        prefix.append(prefix[-1] + a[i])
    tot = prefix[-1]

    # Segment Tree
    tree = [0] * (2 * n + 2)
    def build(arr):
        for i in range(n):
            tree[n + i] = arr[i];
        for i in range(n - 1, 0, -1):
            tree[i] = min(tree[i << 1], tree[i << 1 | 1])
    def updateTreeNode(p, value):
        tree[p + n] = value
        p = p + n
        i = p
        while i > 1:
            tree[i >> 1] = min(tree[i], tree[i ^ 1])
            i >>= 1
    def query(l, r):
        res = float('inf')
        l += n
        r += n
        while l < r:
            if (l & 1):
                res = min(res, tree[l])
                l += 1
            if (r & 1):
                r -= 1
                res = min(res, tree[r])
            l >>= 1
            r >>= 1
        return res

    def check_valid(mid):
        updateTreeNode(0, 0)
        for i in range(n):
            cur_prefix = prefix[i]
            pre_idx = bisect.bisect_left(prefix, cur_prefix - mid)
            valid_min = query(pre_idx, i + 1)
            updateTreeNode(i + 1, valid_min + a[i])
        tail_idx = bisect.bisect_left(prefix, tot - mid)
        tot_valid_min = query(tail_idx, n + 1)
        ans = tot_valid_min <= mid
        return ans

    left = max(a)
    right = prefix[-1]
    while left < right:
        mid = left + (right - left) // 2
        if not check_valid(mid):
            left = mid + 1
        else:
            right = mid

    ans = left
    print(ans)

