import sys
import math
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


def IanandArraySorting():
    n = inp()
    a = inlt()
    odd = 0
    even = 0
    for i in range(n):
        if i % 2 == 1:
            odd += a[i]
        else:
            even += a[i]
    if (n % 2 == 1) or odd >= even:
        print("YES")
    else:
        print("NO")



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        IanandArraySorting()
