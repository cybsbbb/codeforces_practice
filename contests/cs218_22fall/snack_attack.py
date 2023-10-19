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


if __name__ == '__main__':
    n, p, b = inlt()
    r0, c0 = inlt()
    p_dict = collections.defaultdict(int)
    b_dict = collections.defaultdict(int)
    max_t = 0
    for i in range(p):
        r, c, t = inlt()
        p_dict[(r, c, t)] += 1
        max_t = max(max_t, t)
    for i in range(b):
        r, c, t = inlt()
        b_dict[(r, c, t)] += 1
        max_t = max(max_t, t)
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [0, 0]]
    dp_cur = [[-1] * (n) for i in range(n)]
    dp_nxt = [[-1] * (n) for i in range(n)]
    dp_cur[r0][c0] = 0
    cur_t = 1

    while cur_t <= max_t:
        for r in range(n):
            for c in range(n):
                dp_nxt[r][c] = -1
                for direction in directions:
                    r_pre, c_pre = r + direction[0], c + direction[1]
                    if 0 <= r_pre < n and 0 <= c_pre < n and dp_cur[r_pre][c_pre] >= 0:
                        if (r, c, cur_t) in p_dict:
                            dp_nxt[r][c] = max(dp_nxt[r][c], dp_cur[r_pre][c_pre] + p_dict[(r, c, cur_t)])
                        elif (r, c, cur_t) in b_dict:
                            dp_nxt[r][c] = max(dp_nxt[r][c], dp_cur[r_pre][c_pre] // 2)
                        else:
                            dp_nxt[r][c] = max(dp_nxt[r][c], dp_cur[r_pre][c_pre])
        dp_nxt, dp_cur = dp_cur, dp_nxt
        cur_t += 1

    res = 0
    for r in range(n):
        for c in range(n):
            res = max(res, dp_cur[r][c])

    print(res)

