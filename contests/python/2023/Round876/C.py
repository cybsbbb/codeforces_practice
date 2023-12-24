import sys
import heapq
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


def solution():
    n = inp()
    a = inlt()

    if a[-1] == 1:
        print("NO")
        return

    res = []
    ones = 0
    for i in range(n-1)[::-1]:
        if a[i] == 1:
            ones += 1
        if a[i] == 0:
            for i in range(ones):
                res.append(0)
            res.append(ones)
            ones = 0
    for i in range(ones):
        res.append(0)
    res.append(ones)
    print('YES')
    print(' '.join(map(str, res)))
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
