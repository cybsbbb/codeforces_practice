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

def detectiveTask():

    s = insr()
    n = len(s)

    first0 = -1
    last1 = -1

    for i in range(n):
        if s[i] == '?':
            continue
        elif s[i] == '0':
            if last1 == -1:
                print(i + 1)
                return
            else:
                print(i - last1 + 1)
                return
        elif s[i] == '1':
            last1 = i

    if last1 == -1:
        print(n)
        return
    else:
        print(n-last1)
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        detectiveTask()
