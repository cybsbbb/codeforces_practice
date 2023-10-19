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
    s = input().strip()
    n = len(s)
    li = []
    cnt = [[] for _ in range(676)]
    for i in range(n-1):
        cur_val = (ord(s[i]) - ord('a')) * 26 + (ord(s[i+1]) - ord('a'))
        cnt[cur_val].append(i)
        li.append(cur_val)
    # Read the queries
    queries = []
    m = inp()
    ans = [0] * m
    for i in range(m):
        s, t = inlt()
        s -= 1
        t -= 1
        queries.append((s, t))
        ans[i] = abs(t - s)

    # Run BFS on each of the 26*26 and update the best res
    dis = [n] * n
    visited = [False] * n
    flag = [False] * 676
    for i in range(676):
        # Re-init the dis and visited
        for j in range(n):
            dis[j] = n
            visited[j] = False
        for j in range(676):
            flag[j] = False

        # Multi-Source BFS
        q = collections.deque()
        flag[i] = True
        for j in cnt[i]:
            visited[j] = True
            q.append((j, 0))
        while q:
            x, d = q.popleft()
            dis[x] = d
            if x > 0 and visited[x - 1] is False:
                visited[x - 1] = True
                q.append((x - 1, d + 1))
            if x < n-2 and visited[x + 1] is False:
                visited[x + 1] = True
                q.append((x + 1, d + 1))
            if flag[li[x]] is False:
                flag[li[x]] = True
                for y in cnt[li[x]]:
                    if visited[y] is False:
                        visited[y] = True
                        q.append((y, d + 1))

        for j, (s, t) in enumerate(queries):
            ans[j] = min(ans[j], dis[s] + dis[t] + 1)

    for i in ans:
        print(i)


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
