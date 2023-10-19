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

def minimumExtraction():
    n = inp()
    a = sorted(inlt())
    diff = 0
    ret = a[0]
    for i in range(len(a)):
        ret = max(ret, a[i] - diff)
        diff += a[i] - diff
    print(ret)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        minimumExtraction()
