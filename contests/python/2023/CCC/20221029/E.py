import collections
import math
from itertools import combinations
import sys
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
    H, W = inlt()
    grid = []
    for i in range(H):
        grid.append(insr())

    dp = [[False]*W for i in range(H)]
    dp[0][0] = True

    res = 1
    for i in range(1, W):
        if grid[0][i] == '#':
            break
        else:
            dp[0][i] = True
            res = max(res, i + 1)
    for j in range(1, H):
        if grid[j][0] == '#':
            break
        else:
            dp[j][0] = True
            res = max(res, j + 1)

    for i in range(1, H):
        for j in range(1, W):
            if grid[i][j] == '#':
                continue
            else:
                dp[i][j] = dp[i-1][j] | dp[i][j-1]
                if dp[i][j] is True:
                    res = max(res, i+j+1)
    print(res)
