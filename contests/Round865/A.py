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


def IanVisitsMary():
    a, b = inlt()
    if math.gcd(a, b) == 1:
        print(1)
        print(a, b)
    else:
        print(2)
        print(a-1, a-2)
        print(a, b)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        IanVisitsMary()
