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

def divisible25(number):
    tmp1 = 0
    index = len(number) - 1
    while number[index] != '5' and index >= 0:
        index -= 1
        tmp1 += 1
    index -= 1
    while number[index] != '2' and number[index] != '7' and index >= 0:
        index -= 1
        tmp1 += 1

    tmp2 = 0
    index = len(number) - 1
    while number[index] != '0' and index >= 0:
        index -= 1
        tmp2 += 1
    index -= 1
    while number[index] != '5' and number[index] != '0' and index >= 0:
        index -= 1
        tmp2 += 1

    print(min(tmp1, tmp2))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        number = insr()
        divisible25(number)
