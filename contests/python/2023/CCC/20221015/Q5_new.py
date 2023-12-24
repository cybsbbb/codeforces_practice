import collections
import sys
import heapq
input = sys.stdin.readline


def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


if __name__ == '__main__':
    N, M = inlt()

    edges = set()

    dp = [[10000000000] * (N+1) for i in range(N+1)]
    for i in range(1, N+1):
        dp[i][i] = 0
    for i in range(M):
        A, B, C = inlt()
        dp[A][B] = C
        dp[B][A] = C
        edges.add(tuple(sorted((A, B))))

    res = set()

    for k in range(1, N+1):
        for start_idx in range(1, N+1):
            for end_idx in range(1, N+1):
                if k == start_idx or k == end_idx:
                    continue
                tmp = dp[start_idx][k] + dp[k][end_idx]
                if tmp <= dp[start_idx][end_idx]:
                    dp[start_idx][end_idx] = tmp
                    if tuple(sorted((start_idx, end_idx))) in edges:
                        res.add(tuple(sorted((start_idx, end_idx))))

    print(len(res))
