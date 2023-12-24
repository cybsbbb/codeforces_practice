import collections
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


def warehouse():
    n = inp()
    summary = collections.defaultdict(int)
    for i in range(n):
        name, number = input().split()
        number = int(number)
        summary[name] += number
    res = []
    for key, value in summary.items():
        res.append((-value, key))
    res.sort()
    print(len(res))
    for number, name in res:
        print(f"{name} {-number}")
    return 0


if __name__ == '__main__':
    T = inp()
    for i in range(T):
        warehouse()
