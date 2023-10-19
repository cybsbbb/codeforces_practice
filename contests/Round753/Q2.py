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

def oddGrasshopper():
    x, n = inlt()
    for s in range(n//4*4 + 1, n+1):
        if x % 2 == 1:
            x = x + s
        else:
            x = x - s
    print(x)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        oddGrasshopper()
