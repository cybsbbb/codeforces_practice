import bisect
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
    a = inlt()
    q = inp()
    changes = []

    dic = collections.defaultdict(int)
    heap = []
    min_idx = -1

    for i in range(q):
        l, r, diff = inlt()
        l -= 1
        changes.append((l, r, diff))
        dic[l] += diff
        dic[r] -= diff
        if dic[l] == 0:
            del dic[l]
        if dic[r] == 0:
            del dic[r]

        heapq.heappush(heap, l)
        heapq.heappush(heap, r)

        if diff < 0:
            while heap and heap[0] not in dic:
                heapq.heappop(heap)
            if heap and dic[heap[0]] < 0:
                min_idx = i
                dic.clear()
                heap = []

    ans = [0] * (n + 1)
    for i in range(min_idx+1):
        l, r, diff = changes[i]
        ans[l] += diff
        ans[r] -= diff

    for i in range(1, n):
        ans[i] += ans[i-1]
    for i in range(n):
        ans[i] += a[i]
    ans.pop()
    print(*ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
