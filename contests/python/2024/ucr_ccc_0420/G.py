import collections
import math
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
    n, m = inlt()
    matrix = []
    for _ in range(n):
        matrix.append(inlt())
    start = matrix[0][0]
    end = matrix[-1][-1]
    max_gcd = math.gcd(start, end)

    factors = []
    for i in range(1, int(math.sqrt(max_gcd)) + 1):
        if max_gcd % i == 0:
            factors.append(i)
            factors.append(max_gcd // i)
    factors.sort(reverse=True)



    dp = [[0] * m for _ in range(n)]
    def helper(factor):
        for i in range(n):
            for j in range(m):
                dp[i][j] = 0
        dp[0][0] = 1
        for i in range(1, n):
            if dp[i - 1][0] and matrix[i][0] % factor == 0:
                dp[i][0] = 1
            else:
                break
        for j in range(1, m):
            if dp[0][j - 1] and matrix[0][j] % factor == 0:
                dp[0][j] = 1
            else:
                break

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] % factor == 0 and (dp[i][j - 1] or dp[i-1][j]):
                    dp[i][j] = 1

        return dp[n - 1][m - 1]


    for factor in factors:
        if helper(factor):
            print(factor)
            return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
