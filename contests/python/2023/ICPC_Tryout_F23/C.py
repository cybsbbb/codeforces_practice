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
    n, m, q, l = inlt()
    graph = collections.defaultdict(list)
    for i in range(m):
        a, b, c = inlt()
        graph[a].append((b, c))
        graph[b].append((a, c))

    queue = [(-l, 1)]
    remainings = [0] * (n + 1)
    remainings[1] = l

    while queue:
        cur_remain, cur_node = heapq.heappop(queue)
        cur_remain = -cur_remain
        for nxt_node, road_type in graph[cur_node]:
            if road_type == 1:
                nxt_remaining = cur_remain - 1
            else:
                nxt_remaining = cur_remain // 2
            if nxt_remaining > remainings[nxt_node]:
                remainings[nxt_node] = nxt_remaining
                heapq.heappush(queue, (-nxt_remaining, nxt_node))

    print(remainings)
    for _ in q:
        query = inp()
        if remainings[query] == 0:
            print("Large")
        else:
            print(l-remainings[query] + 1)

    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
