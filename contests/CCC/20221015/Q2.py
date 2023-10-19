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
    A = inlt()
    B = inlt()
    res = 0
    for i in range(N):
        if A[i] == B[i]:
            res += 1

    print(res)
    print(len(set(A) & set(B)) - res)
