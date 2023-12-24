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
    N = inp()
    if N <= 125:
        print(4)
    elif 125 < N <= 211:
        print(6)
    elif N > 211:
        print(8)
