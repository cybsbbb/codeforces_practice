import collections
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


def TheLakes():
    n, m = inlt()
    lake = []
    for i in range(n):
        lake.append(inlt())
    used = [[False] * m for _ in range(n)]

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    res = 0

    for i in range(n):
        for j in range(m):
            if used[i][j] == False and lake[i][j] != 0:
                used[i][j] = True
                todo = [(i, j)]
                tmp_res = 0
                while todo:
                    x, y = todo.pop()
                    tmp_res += lake[x][y]
                    for dx, dy in directions:
                        xx = x + dx
                        yy = y + dy
                        if 0 <= xx < n and 0 <= yy < m and used[xx][yy] == False and lake[xx][yy] > 0:
                            todo.append((xx, yy))
                            used[xx][yy] = True
                res = max(res, tmp_res)
    print(res)
    return res


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        TheLakes()
