import itertools
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
    N, X, Y = inlt()
    A = inlt()
    B = inlt()
    idxs = itertools.permutations(range(N))
    for idx in idxs:
        print(idx)
