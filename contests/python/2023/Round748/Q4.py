import sys
import math
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

def allaresame(n, numbers):
    numbers = sorted(list(set(numbers)))
    if len(numbers) == 1:
        print("-1")
        return
    ret = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        ret = math.gcd(ret, numbers[i] - numbers[i-1])
        if ret == 1:
            break
    print(ret)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        n = inp()
        numbers = inlt()
        allaresame(n, numbers)
