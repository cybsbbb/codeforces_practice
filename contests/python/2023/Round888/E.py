
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
    n, k = inlt()
    c = inlt()
    p = inlt()
    p_set = set(p)
    graph = collections.defaultdict(list)
    mix_option = dict()
    nodes_in = collections.defaultdict(int)
    for i in range(1, n+1):
        tmp = inlt()
        m = tmp[0]
        e = tmp[1:]
        mix_option[i] = e
        if i not in p_set:
            for potion in e:
                graph[potion].append(i)
                nodes_in[i] += 1
    res = {i: c[i-1] for i in range(1, n+1)}
    for free in p:
        res[free] = 0

    q = collections.deque()
    for i in range(1, n+1):
        if nodes_in[i] == 0:
            q.append(i)

    while len(q) > 0:
        cur_node = q.popleft()
        if len(mix_option[cur_node]) > 0:
            res[cur_node] = min(res[cur_node], sum(res[potion] for potion in mix_option[cur_node]))
        for nxt_node in graph[cur_node]:
            nodes_in[nxt_node] -= 1
            if nodes_in[nxt_node] == 0:
                q.append(nxt_node)

    res_list = list([res[i] for i in range(1, n+1)])
    print(' '.join(map(str, res_list)))


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
