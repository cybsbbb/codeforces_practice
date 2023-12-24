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


def solution():
    n, m = inlt()
    matrix = []
    for i in range(n):
        matrix.append(insr())
    tot_empty = 0
    vova_i, vova_j = 0, 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '.':
                tot_empty += 1
            if matrix[i][j] == 'V':
                vova_i, vova_j = i, j
                matrix[i][j] = '.'

    def get_idx(i, j):
        return i * m + j

    # 1. time, 2. last exit, 3 distance
    information = [[[0] * 3 for _ in range(m)] for _ in range(n)]
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    cur_layer = []
    dis = 0
    for j in range(1, m-1):
        if matrix[0][j] == '.':
            cur_layer.append((0, j, get_idx(0, j)))
            information[0][j][0] += 1
            information[0][j][1] = get_idx(0, j)
        if matrix[n-1][j] == '.':
            cur_layer.append((n-1, j, get_idx(n-1, j)))
            information[n-1][j][0] += 1
            information[n-1][j][1] = get_idx(n-1, j)
    for i in range(1, n-1):
        if matrix[i][0] == '.':
            cur_layer.append((i, 0, get_idx(i, 0)))
            information[i][0][0] += 1
            information[i][0][1] = get_idx(i, 0)
        if matrix[i][m-1] == '.':
            cur_layer.append((i, m-1, get_idx(i, m-1)))
            information[i][m-1][0] += 1
            information[i][m-1][1] = get_idx(i, m-1)

    while cur_layer:
        nxt_layer = []
        dis += 1
        for cur_i, cur_j, cur_exit in cur_layer:
            for ii, jj in directions:
                nxt_i, nxt_j = cur_i + ii, cur_j + jj
                if 0 <= nxt_i < n and 0 <= nxt_j < m and matrix[nxt_i][nxt_j] == '.' and information[nxt_i][nxt_j][0] < 2 and information[nxt_i][nxt_j][1] != cur_exit:
                    nxt_layer.append((nxt_i, nxt_j, cur_exit))
                    information[nxt_i][nxt_j][0] += 1
                    information[nxt_i][nxt_j][1] = cur_exit
                    information[nxt_i][nxt_j][2] += dis
        cur_layer = nxt_layer

    if information[vova_i][vova_j][0] == 0:
        print(tot_empty)
        return
    if information[vova_i][vova_j][0] == 1:
        print(tot_empty - information[vova_i][vova_j][2])
        return

    cur_layer = [(vova_i, vova_j)]
    dis = 0
    seen = set()
    seen.add((vova_i, vova_j))
    ans = information[vova_i][vova_j][2]

    while cur_layer:
        nxt_layer = []
        dis += 1
        for cur_i, cur_j in cur_layer:
            for ii, jj in directions:
                nxt_i, nxt_j = cur_i + ii, cur_j + jj
                if 0 <= nxt_i < n and 0 <= nxt_j < m and (nxt_i, nxt_j) not in seen and matrix[nxt_i][nxt_j] == '.' and information[nxt_i][nxt_j][0] == 2:
                    ans = min(ans, dis + information[nxt_i][nxt_j][2])
                    nxt_layer.append((nxt_i, nxt_j))
                    seen.add((nxt_i, nxt_j))
        cur_layer = nxt_layer

    print(tot_empty - ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
