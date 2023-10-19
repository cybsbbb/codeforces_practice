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


def LunaticNeverContent():
    n = inp()
    a = inlt()

    if a[0] == a[-1]:
        cur_max = float('inf')
    else:
        cur_max = abs(a[0] - a[-1])
    for i in range(1, n//2):
        if a[0+i] == a[-1-i]:
            continue
        else:
            if cur_max == float('inf'):
                cur_max = abs(a[0+i] - a[-1-i])
            else:
                cur_max = math.gcd(abs(a[0 + i] - a[-1 - i]), cur_max)

    if cur_max == float('inf'):
        print(0)
        return
    else:
        print(cur_max)
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        LunaticNeverContent()
