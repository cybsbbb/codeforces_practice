import collections
import sys
import math
import heapq

input = sys.stdin.readline


def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))
def insr():
    s = input()
    return (list(s[:len(s) - 1]))
def invr():
    return (map(int, input().split()))


def solution():
    n = inp()
    a = inlt()
    divides = []
    for i in range(1, n + 1):
        if n % i == 0:
            divides.append(i)
    ans = 1

    for divide in divides[:-1]:
        length = n // divide
        flag = False
        gcd = 0
        for i in range(divide):
            for j in range(1, length):
                cur_interval = abs(a[j * divide + i] - a[(j-1) * divide + i])
                if cur_interval != 0:
                    if flag is False:
                        gcd = cur_interval
                        flag = True
                    else:
                        gcd = math.gcd(gcd, cur_interval)

        if flag is False or gcd > 1:
            ans += 1

    print(ans)
    return ans


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
