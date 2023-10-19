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
    n, s = list(map(int, input().strip().split()))
    ts = list(map(int, input().strip().split()))

    # million_s = max(sum(ts), max(ts) * s + 1)
    million_s = max(ts) * s
    print((million_s-1) // 1000 + 1)
