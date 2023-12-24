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


def banquetPreparations():
    input()
    n, m = inlt()
    dishes = []
    for i in range(n):
        dishes.append(inlt())

    ret = 0
    ret_dishes = []

    for i in range(n):
        total = dishes[i][0] + dishes[i][1]
        remaining = total - m



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        banquetPreparations()

