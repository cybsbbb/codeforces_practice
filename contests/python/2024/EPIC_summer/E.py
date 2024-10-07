import collections
import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    a = (list(map(int, input().split())))
    p = [0] + (list(map(int, input().split())))
    tree = [[] for _ in range(n)]
    children_sum = [0] * n
    ins = [0] * n
    for i in range(1, n):
        tree[p[i] - 1].append(i)
        children_sum[p[i] - 1] += a[i]
        ins[p[i] - 1] += 1
    topology = collections.deque()
    for i in range(n):
        if ins[i] == 0:
            topology.append(i)

    ans = 0
    while topology:
        node = topology.popleft()
        if len(tree[node]) != 0:
            cur_val = a[node]
            child_sum = children_sum[node]
            if cur_val > child_sum:
                target = cur_val - child_sum
                bfs = collections.deque()
                for child in tree[node]:
                    bfs.append(child)
                changed_nodes = []
                depth = 1
                while bfs:
                    for _ in range(len(bfs)):
                        bfs_node = bfs.popleft()
                        changed_nodes.append(bfs_node)
                        if len(tree[bfs_node]) == 0:
                            ans += target * depth
                            a[bfs_node] += target
                            children_sum[p[bfs_node] - 1] += target
                            # while bfs_node != node:
                            #     a[bfs_node] += target
                            #     children_sum[p[bfs_node] - 1] += target
                            #     bfs_node = p[bfs_node] - 1
                            target = 0
                            break
                        else:
                            bfs_val = a[bfs_node]
                            bfs_child_sum = children_sum[bfs_node]
                            if bfs_val < bfs_child_sum:
                                tmp = min(bfs_child_sum - bfs_val, target)
                                target -= tmp
                                ans += tmp * depth
                                a[bfs_node] += tmp
                                children_sum[p[bfs_node] - 1] += tmp
                            for bfs_child in tree[bfs_node]:
                                bfs.append(bfs_child)
                        if target == 0:
                            break
                    if target == 0:
                        break
                    depth += 1

                for bfs_node in changed_nodes[::-1]:
                    if a[bfs_node] < children_sum[bfs_node]:
                        delta = children_sum[bfs_node] - a[bfs_node]
                        a[bfs_node] += delta
                        children_sum[p[bfs_node] - 1] += delta
                if a[node] < children_sum[node]:
                    delta = children_sum[node] - a[node]
                    a[node] += delta
                    if p[node] - 1 >= 0:
                        children_sum[p[node] - 1] += delta


        parent = p[node] - 1
        ins[parent] -= 1
        if ins[parent] == 0:
            topology.append(parent)

    print(ans)
    return


for _ in range(int(input())):
    solve()

