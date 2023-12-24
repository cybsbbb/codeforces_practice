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


def beast_bullies(n, animals):
    if n == 1:
        print(1)
        return 0
    animals.sort(reverse=True)
    res = 1
    big = animals[0]
    small = 0
    for i in range(1, n):
        small += animals[i]
        if small >= big:
            res = i + 1
            big += small
            small = 0
    print(res)
    return 0


if __name__ == '__main__':
    n = inp()
    animals = []
    for i in range(n):
        animals.append(inp())
    beast_bullies(n, animals)
