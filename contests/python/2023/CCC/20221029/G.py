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
    s = insr()
    t = insr()
    n = len(s)
    flag = True
    dis = ord(s[0]) - ord(t[0])

    for i in range(n):
        if (ord(t[i]) - ord('a') + dis) % 26 + ord('a') != ord(s[i]):
            print("No")
            flag = False
            break

    if flag is True:
        print("Yes")
