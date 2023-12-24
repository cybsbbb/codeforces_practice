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
    S, T = inlt()
    res = 0
    for first in range(0, S+1):
        for second in range(0, S+1):
            for third in range(0, S+1):
                if first + second + third <= S and  first * second * third <= T:
                    res += 1
    print(res)


