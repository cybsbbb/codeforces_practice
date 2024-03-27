import collections
import sys
import math
import heapq
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


t = inp()
for _ in range(t):
    n, k = inlt()
    tree = collections.defaultdict(list)
    for _ in range(n - 1):
        u, v = inlt()
        u -= 1
        v -= 1
        tree[u].append(v)
        tree[v].append(u)

    upper = n // (k + 1)
    if upper == 1:
        print(1)
        continue

    components = 0


    @bootstrap
    def check(cur_node, parent, mid):
        global components
        cur_cnt = 1
        for nxt_node in tree[cur_node]:
            if nxt_node == parent:
                continue
            cur_cnt += yield check(nxt_node, cur_node, mid)
        if cur_cnt >= mid:
            components += 1
            yield 0
        else:
            yield cur_cnt

    left = 1
    right = upper
    while left < right:
        mid = (left + right + 1) // 2
        components = 0
        check(0, -1, mid)
        if components >= (k + 1):
            left = mid
        else:
            right = mid - 1
    print(left)

