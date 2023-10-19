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
    q = inp()
    x = inlt()
    head = x[0]
    cur = x[0]
    decreased = False
    res = ['1']

    for num in x[1:]:
        if num >= cur:
            if decreased == False:
                res.append('1')
                cur = num
            elif decreased == True:
                if num <= head:
                    res.append('1')
                    cur = num
                else:
                    res.append('0')
        else:
            if decreased == True:
                res.append('0')
            else:
                if num <= head:
                    decreased = True
                    res.append('1')
                    cur = num
                else:
                    res.append('0')

    print(''.join(res))
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
