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


def NotAdjacentMatrix(n):
    if n == 1:
        print(1)
        return
    if n == 2:
        print(-1)
        return
    tmp = []
    for i in range(1, n*n+1, 2):
        tmp.append(str(i))
        if len(tmp) == n:
            print(' '.join(tmp))
            tmp = []
    for i in range(2, n*n+1, 2):
        tmp.append(str(i))
        if len(tmp) == n:
            print(' '.join(tmp))
            tmp = []
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        n = inp()
        NotAdjacentMatrix(n)
