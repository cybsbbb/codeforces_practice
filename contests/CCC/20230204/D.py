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


def ghost_leg(n, m, rungs):
    res = [0] * n
    for i in range(1, n+1):
        cur_loc = i
        for rung in rungs:
            nxt_loc = cur_loc
            if rung == cur_loc:
                nxt_loc += 1
            elif rung == cur_loc - 1:
                nxt_loc -= 1
            cur_loc = nxt_loc
        res[cur_loc-1] = i

    for loc in res:
        print(loc)
    return 0


if __name__ == '__main__':
    n, m = inlt()
    rungs = []
    for i in range(m):
        rungs.append(inp())
    ghost_leg(n, m, rungs)
