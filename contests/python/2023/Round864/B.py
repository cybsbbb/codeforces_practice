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

def Pattern():
    n, k = inlt()
    maze = [[0]*n for _ in range(n)]
    for i in range(n):
        row = inlt()
        for j in range(n):
            maze[i][j] = row[j]

    unmatch = 0
    for i in range(n):
        for j in range(n):
            if maze[i][j] != maze[-(i+1)][-(j+1)]:
                unmatch += 1
    unmatch = unmatch // 2

    if k < unmatch:
        print("NO")
        return
    else:
        if n % 2 == 1:
            print("YES")
            return
        k -= unmatch
        if k % 2 == 0:
            print("YES")
            return
        else:
            print("NO")
            return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        Pattern()
