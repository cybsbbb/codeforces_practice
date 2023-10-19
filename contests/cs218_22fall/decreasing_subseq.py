import collections
import bisect
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


if __name__ == '__main__':
    t = inp()
    seq = inlt()
    seq = seq[::-1]

    sub = []
    for num in seq:
        i = bisect.bisect_left(sub, num)
        if i == len(sub):
            sub.append(num)
        else:
            sub[i] = num

    print(len(sub))
