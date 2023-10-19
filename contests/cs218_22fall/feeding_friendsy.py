import collections
import bisect
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


def status2score(status):
    if status[1] > 0:
        pre_score = 3
    elif status[0] > 0:
        pre_score = 1
    else:
        pre_score = 0
    return pre_score


if __name__ == '__main__':
    T, n, m = inlt()

    edges = []
    for i in range(n):
        a, b, c = inlt()
        edges.append([a, False, bool(c)])
        edges.append([b, True, bool(c)])
    for i in range(m):
        a, b, c = inlt()
        edges.append([a, False, bool(c)])
        edges.append([b, True, bool(c)])
    edges.sort()

    res = 0
    status = [0, 0]

    pre_idx = edges[0][0]
    status[edges[0][2]] += 1
    pre_score = status2score(status)
    res += pre_score

    for edge in edges[1:]:
        res += pre_score * (edge[0] - pre_idx)
        if edge[1] == 0:
            status[edge[2]] += 1
        else:
            status[edge[2]] -= 1
        cur_score = status2score(status)
        if cur_score > pre_score:
            res += cur_score - pre_score

        pre_idx = edge[0]
        pre_score = cur_score

    print(res)
