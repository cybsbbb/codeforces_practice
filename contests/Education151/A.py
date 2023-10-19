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


def solution():
    n, k, x = inlt()

    if k == 1:
        print("No")

    if k > 1 and x != 1:
        print("Yes")
        print(n)
        print(' '.join(['1']*n))

    if k > 1 and x == 1:
        if k == 2:
            if n % 2 == 1:
                print("No")
            if n % 2 == 0:
                print("Yes")
                print(n//2)
                print(' '.join(['2'] * (n//2)))
        else:
            if n % 2 == 1:
                print("Yes")
                print((n-3)//2 + 1)
                print(' '.join(['3'] + ['2'] * ((n-3) // 2)))
            if n % 2 == 0:
                print("Yes")
                print(n//2)
                print(' '.join(['2'] * (n//2)))


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
