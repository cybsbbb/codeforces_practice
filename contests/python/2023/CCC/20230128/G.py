import collections
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


def last_factorial_digit(n):
    res = 1
    for i in range(1, n+1):
        res *= i
        res %= 10
    print(res)


if __name__ == '__main__':
    T = inp()
    for i in range(T):
        n = inp()
        last_factorial_digit(n)
