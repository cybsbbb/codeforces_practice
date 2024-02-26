import sys
import heapq
import collections
from types import GeneratorType

input = sys.stdin.readline

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

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
    c = inlt()
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = inlt()
        tree[v - 1].append(u - 1)
        tree[u - 1].append(v - 1)
    ans = [0]
    @bootstrap
    def dfs(cur_node, parent):
        cur_cnt = collections.defaultdict(int)
        for nxt_node in tree[cur_node]:
            if nxt_node == parent:
                continue
            nxt_cnt = yield dfs(nxt_node, cur_node)
            if c[cur_node] in nxt_cnt:
                ans[0] += nxt_cnt[c[cur_node]]
                del nxt_cnt[c[cur_node]]
            if len(nxt_cnt) > len(cur_cnt):
                cur_cnt, nxt_cnt = nxt_cnt, cur_cnt
            for clr, v in nxt_cnt.items():
                ans[0] += v * cur_cnt[clr]
                cur_cnt[clr] += v
        cur_cnt[c[cur_node]] += 1
        yield cur_cnt

    dfs(0, -1)
    print(ans[0])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
