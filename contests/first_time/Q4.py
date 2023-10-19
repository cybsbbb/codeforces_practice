import sys
input = sys.stdin.readline
from collections import defaultdict

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def SameDifferences(n, l):
    groups = defaultdict(list)
    for i in range(n):
        groups[l[i] - i].append(i)

    res = 0
    for key in groups:
        if len(groups[key]) > 1:
            res += len(groups[key]) * (len(groups[key]) - 1) //2

    print(res)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        n = inp()
        l = inlt()
        SameDifferences(n, l)
