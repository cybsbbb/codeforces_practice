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


def LoveStory():
    base_s = 'codeforces'
    s = insr()
    res = 0
    for i in range(len(base_s)):
        if base_s[i] != s[i]:
            res += 1
    print(res)
    return res


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        LoveStory()
