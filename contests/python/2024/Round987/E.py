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


def solution():
    n = inp()
    p = [0] + inlt()
    for i in range(n):
        p[i] -= 1
    tree = [[] for _ in range(n)]
    for i in range(1, n):
        tree[p[i]].append(i)
    res = [-1] * n
    st = []
    st.append((0, False))
    while st:
        cur_node, cur_flag = st.pop()
        if cur_flag is False:
            st.append((cur_node, True))
            for nxt_node in tree[cur_node]:
                st.append((nxt_node, False))
        else:
            tmp = []
            for nxt_node in tree[cur_node]:
                heapq.heappush(tmp, res[nxt_node])
            if len(tmp) == 0:
                res[cur_node] = 0
            else:
                while len(tmp) > 2:
                    node1 = heapq.heappop(tmp)
                    node2 = heapq.heappop(tmp)
                    heapq.heappush(tmp, max(node1, node2) + 1)
                res[cur_node] = tmp[-1] + 1
    print(res[0])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
