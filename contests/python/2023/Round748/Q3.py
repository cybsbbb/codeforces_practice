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

def savemoremice(n, k, mices):
    mices.sort()
    ret = 0
    cat = 0
    for mice in mices[::-1]:
        if cat >= mice:
            break
        cat += n - mice
        if cat < n:
            ret += 1
        if cat >= n:
            break
    print(ret)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        n, k = inlt()
        mices = inlt()
        savemoremice(n, k, mices)
