import collections
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


def metronome(n):
    res = n // 4
    res += (n % 4) * 0.25
    print(res)
    return 0


if __name__ == '__main__':
    n = inp()
    metronome(n)