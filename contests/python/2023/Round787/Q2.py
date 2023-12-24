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

def makeitIncreasing():

    n = inp()
    a = inlt()
    res = 0

    for i in range(n-1)[::-1]:
        while a[i] >= a[i+1] and a[i] != 0:
            a[i] = a[i] // 2
            res = res + 1

        if a[i] == 0 and i > 0:
            print(-1)
            return

        if a[i] == 0 and a[i] == a[i+1]:
            print(-1)
            return

    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        makeitIncreasing()
