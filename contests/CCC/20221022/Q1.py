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
    k = inp()
    my = list(input().strip())
    friend = list(input().strip())

    n = len(my)
    same = 0
    for i in range(n):
        if my[i] == friend[i]:
            same += 1

    diff = n - same
    wrong = n - k
    print(min(same, k) + min(wrong, diff))
