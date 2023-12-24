import collections
import sys
import math
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


def ForeverWinter():
    n, m = inlt()
    graph = collections.defaultdict(list)
    for _ in range(m):
        u, v = inlt()
        graph[u].append(v)
        graph[v].append(u)

    counter = collections.defaultdict(int)
    for key in graph:
        counter[len(graph[key])] += 1

    xy = counter[1]
    if len(counter) == 3:
        for key in counter:
            if counter[key] == 1:
                x = key
                y = xy // x
                print(x, y)
                return
    elif len(counter) == 2:
        for key in counter:
            if key != 1:
                x = counter[key]-1
                y = xy // x
                print(x, y)
                return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        ForeverWinter()
