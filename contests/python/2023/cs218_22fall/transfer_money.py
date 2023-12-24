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
    n, m = inlt()
    graph = collections.defaultdict(list)
    rate_dict = collections.defaultdict(int)
    for i in range(m):
        x, y, z = inlt()
        graph[x].append((y, z))
        graph[y].append((x, z))
        rate_dict[x] = 0
        rate_dict[y] = 0
    src, des = inlt()

    rate_dict[src] = 1
    while len(rate_dict) > 0:
        max_peo = max(rate_dict, key=rate_dict.get)
        if max_peo == des:
            print(100 / rate_dict[max_peo])
            break
        max_rate = rate_dict[max_peo]
        for nxt_peo, fee in graph[max_peo]:
            rate_dict[nxt_peo] = max(rate_dict[nxt_peo], max_rate * (100-fee)/100)
        rate_dict.pop(max_peo)
