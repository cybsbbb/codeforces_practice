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
    n = inp()
    a = inlt()
    price = 0
    max_price = 0
    max_diff = 0
    res = 0
    for i in range(n):
        price += a[i]
        if price > max_price:
            max_price = price
        if max_price - price > max_diff:
            max_diff = max_price - price
            res = max_price

    print(res)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
