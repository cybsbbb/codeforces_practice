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
    n = inp()
    p = [-1] + inlt()
    # 0-index
    tree = [[] for i in range(n)]
    for i in range(1, n):
        tree[p[i] - 1].append(i)

    counts = [0] * n

    stack = [(0, 0)]
    while stack:
        cur_node, state = stack.pop()
        if state == 0:
            counts[cur_node] += 1
            stack.append((cur_node, 1))
            for nxt_node in tree[cur_node]:
                stack.append((nxt_node, 0))
        if state == 1:
            for nxt_node in tree[cur_node]:
                counts[cur_node] += counts[nxt_node]

    ans = 0
    cur_node = 0
    matched = 0
    while len(tree[cur_node]) > 0:
        matched = max(matched - 1, 0)
        stat = sorted([[cur_node, counts[cur_node]] for cur_node in tree[cur_node]], key=lambda x: x[1], reverse=True)
        if len(stat) == 1:
            cur_node = stat[0][0]
            continue
        max_node, max_count = stat[0]
        tot_sub_nodes = counts[cur_node] - 1
        if max_count - matched <= tot_sub_nodes - max_count:
            ans += (tot_sub_nodes - matched) // 2
            break
        else:
            ans += (tot_sub_nodes - max_count)
            matched += tot_sub_nodes - max_count
            cur_node = max_node
            continue
    print(ans)
    return ans


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
