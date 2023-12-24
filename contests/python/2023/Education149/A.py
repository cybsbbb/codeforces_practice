import collections
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


def grasshopper():
    x, k = inlt()
    if x % k != 0:
        print(1)
        print(x)
        return
    else:
        print(2)
        print(x+1, -1)
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        grasshopper()
