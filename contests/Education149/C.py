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
    s = insr()
    n = len(s)
    cur = '0'
    res = []
    for i in range(n):
        if s[i] == '0':
            cur = '0'
            res.append(s[i])
        elif s[i] == '1':
            cur = '1'
            res.append(s[i])
        elif s[i] == '?':
            if cur == '0':
                res.append('0')
            elif cur == '1':
                res.append('1')

    print(''.join(res))



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
