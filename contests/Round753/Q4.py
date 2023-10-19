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

def blueRedPermutation():
    n = inp()
    a = inlt()
    s = insr()
    red = []
    blue = []
    for i in range(n):
        if s[i] == 'B':
            blue.append(a[i])
        else:
            red.append(a[i])
    blue.sort()
    red.sort()
    for i in range(len(blue)):
        if blue[i] < i+1:
            print("NO")
            return
    for i in range(len(red)):
        if red[-1-i] > n-i:
            print("NO")
            return
    print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        blueRedPermutation()
