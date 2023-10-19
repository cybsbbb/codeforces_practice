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
    V, A, B, C = inlt()
    tot = A + B + C
    V = V % tot
    V = V - A
    if V < 0:
        print("F")
    else:
        V = V - B
        if V < 0:
            print("M")
        else:
            print("T")
