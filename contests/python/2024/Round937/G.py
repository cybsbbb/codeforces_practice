import collections
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


def solution():
    n = inp()
    genre_idx = 0
    writer_idx = 0
    genre_idx_map = dict()
    writer_idx_map = dict()
    graph = collections.defaultdict(list)

    genre_idx_nodes = collections.defaultdict(list)
    writer_idx_nodes = collections.defaultdict(list)
    for i in range(n):
        gi, wi = input()[:-1].split()
        if gi not in genre_idx_map:
            genre_idx_map[gi] = genre_idx
            genre_idx += 1
        if wi not in writer_idx_map:
            writer_idx_map[wi] = writer_idx
            writer_idx += 1
        for node in genre_idx_nodes[genre_idx_map[gi]]:
            graph[i].append(node)
            graph[node].append(i)
        genre_idx_nodes[genre_idx_map[gi]].append(i)
        for node in writer_idx_nodes[writer_idx_map[wi]]:
            graph[i].append(node)
            graph[node].append(i)
        writer_idx_nodes[writer_idx_map[wi]].append(i)

    def helper(cur, mask, depth):
        mask |= 1 << cur
        if (cur << n) + mask in memo:
            return memo[(cur << n) + mask]

        max_depth = depth
        for nxt in graph[cur]:
            if mask & (1 << nxt):
                continue
            max_depth = max(max_depth, helper(nxt, mask, depth + 1))

        memo[(cur << n) + mask] = max_depth
        return max_depth

    memo = {}
    ans = n - max(helper(root, 0, 1) for root in range(n))
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
