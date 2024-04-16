import heapq
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


t = inp()
for _ in range(t):
    n, k = inlt()
    a = []
    for i in range(n):
        a.append(inlt())

    dp = [[] for _ in range(n + 2)]
    dp[-1].append(0)
    dp[-2].append(0)
    dp[0].append(0)
    dp[0].append(a[0][0])
    dp[0].sort(reverse=True)

    for i in range(1, n):
        aj = [a[j + 2][i - j - 2] for j in range(i - 1)]
        aj.append(0)
        indexes = [0] * i

        heap_tmp = []
        heapq.heappush(heap_tmp, (-a[0][i], -2))
        heapq.heappush(heap_tmp, (-a[1][i - 1], -1))
        for j in range(i):
            heapq.heappush(heap_tmp, (-(dp[j][0] + aj[j]), j))

        while heap_tmp and len(dp[i]) < k:
            cur_val, j = heapq.heappop(heap_tmp)
            dp[i].append(-cur_val)
            if j >= 0 and indexes[j] + 1 < len(dp[j]):
                heapq.heappush(heap_tmp, (-(dp[j][indexes[j] + 1] + aj[j]), j))
                indexes[j] += 1

    print(*dp[n - 1][:k])
