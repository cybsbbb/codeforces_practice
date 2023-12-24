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


def GoldRush():
    n, m = inlt()
    if n == m:
        print("YES")
        return
    if n % 3 != 0 and n != m:
        print("NO")
        return
    divide_mid_values = set()
    divide_times = 0
    while n % 3 == 0:
        n = n // 3
        divide_mid_values.add(n)
        divide_times += 1

    if m in divide_mid_values:
        print("YES")
        return

    while m % 2 == 0 and divide_times > 0:
        m = m // 2
        divide_times -= 1
        if m in divide_mid_values:
            print("YES")
            return
    print("NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        GoldRush()
