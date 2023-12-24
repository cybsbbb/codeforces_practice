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

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()
    res = 0
    for i in range(n):
        for j in range(m):
            if lake[i][j] == 0:
                visited.add((i, j))
                continue
            if lake[i][j] > 0 and (i, j) not in visited:
                visited.add((i, j))
                tmp_res = lake[i][j]
                cur_layer = [(i, j)]
                while len(cur_layer) > 0:
                    nxt_layer = []
                    for x, y in cur_layer:
                        for dx, dy in directions:
                            xx, yy = x + dx, y + dy
                            if (0 <= xx < n) and (0 <= yy < m) and lake[xx][yy] > 0 and ((xx, yy) not in visited):
                                visited.add((xx, yy))
                                tmp_res += lake[xx][yy]
                                nxt_layer.append((xx, yy))
                    cur_layer = nxt_layer
                res = max(res, tmp_res)
    print(res)
    return res


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        TheLakes()
