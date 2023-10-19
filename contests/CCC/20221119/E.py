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
    K = inp()
    desks = []
    for i in range(K):
        desks.append(inp())
    res = 1
    n = len(desks)
    for idx in range(1, n):
        if desks[idx] < desks[idx-1]:
            res += 1
    print(res)


