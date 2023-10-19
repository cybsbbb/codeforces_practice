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
    N, X = inlt()
    moves = list(insr())
    uppers = 0
    childs = []
    for move in moves:
        if move == 'U':
            if len(childs) == 0:
                uppers += 1
            else:
                childs.pop()
        else:
            childs.append(move)

    for i in range(uppers):
        X = X // 2
    for child in childs:
        if child == 'L':
            X = X * 2
        else:
            X = X * 2 + 1

    print(X)
