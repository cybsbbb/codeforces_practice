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

def suspicious(n, s):
    seen = set()
    seen.add(s[0])
    for i in range(1, n):
        if s[i] != s[i-1] and s[i] in seen:
            print("NO")
            return
        seen.add(s[i])
    print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        n = inp()
        s = insr()
        suspicious(n, s)
