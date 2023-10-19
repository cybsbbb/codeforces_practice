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


def DreamingofFreedom():
    n, m = inlt()

    # for i in range(1, min(n, int(math.sqrt(n))+1)):
    #     if n % i == 0:
    #         for x in [i, n//i]:
    #             if 1 < x <= m:
    #                 print("NO")
    #                 return
    #
    # print("YES")
    # return

    if n == 1 or m == 1:
        print("YES")
        return
    if n <= m:
        print("NO")
        return
    if n % 2 == 0:
        if m > 1:
            print("NO")
            return
    elif n % 2 == 1:
        for i in range(3, min(n, int(math.sqrt(n))+1)):
            if n % i == 0 and m >= i:
                print("NO")
                return
    print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        DreamingofFreedom()
