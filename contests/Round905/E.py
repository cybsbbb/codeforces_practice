import bisect
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
    n, t = inlt()
    graph = [[] for _ in range(n+1)]
    for moment in range(1, t+1):
        mi = inp()
        for _ in range(mi):
            v, u = inlt()
            graph[u].append((moment, v))
            graph[v].append((moment, u))
    k = inp()
    a = inlt()

    time_stamps = [[] for _ in range(t+1)]
    for i in range(k):
        time_stamps[a[i]].append(i)

    heap = []
    heapq.heappush(heap, (0, 1))
    seen = set()

    while heap:
        cur_time, cur_loc = heapq.heappop(heap)
        if cur_loc in seen:
            continue
        if cur_loc == n:
            print(cur_time)
            return
        seen.add(cur_loc)
        for moment, nxt_loc in graph[cur_loc]:
            nxt_time_idx = bisect.bisect_left(time_stamps[moment], cur_time)
            if nxt_time_idx < len(time_stamps[moment]):
                heapq.heappush(heap, (time_stamps[moment][nxt_time_idx] + 1, nxt_loc))

    print(-1)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
