import collections
import bisect
import heapq
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
    for i in range(t):
        n = inp()
        peels = inlt()
        peels = sorted(peels)
        min_peel = peels[0]
        res = 0
        for peel in peels[1:]:
            if peel < 2*min_peel:
                continue
            else:
                n = (peel - 1) // (2 * min_peel-1) + 1
                if ((peel - 1) // n + 1) < min_peel:
                    res += n-2
                else:
                    res += n-1
        print(res)
