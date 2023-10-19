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


def ArrangingTheSheep(n, s):
    left = [0]*n
    right = [0]*n

    sheep_num = 0
    total_move = 0
    for i in range(n):
        if s[i] == '*':
            sheep_num += 1
        else:
            total_move += sheep_num
        left[i] = total_move

    sheep_num = 0
    total_move = 0
    for i in range(n-1, -1, -1):
        if s[i] == '*':
            sheep_num += 1
        else:
            total_move += sheep_num
        right[i] = total_move

    res = left[0] + right[0]
    for i in range(n):
        res = min(res, left[i] + right[i])
    print(res)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        n = inp()
        s = insr()
        ArrangingTheSheep(n, s)
