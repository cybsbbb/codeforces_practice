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


def comparison():
    n = inp()
    s = insr()

    cur_len = 1
    max_len = 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            cur_len += 1
            max_len = max(max_len, cur_len)
        else:
            cur_len = 1

    max_len = max(max_len, cur_len)
    print(max_len + 1)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        comparison()
