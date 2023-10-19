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


def aPerfectlyBalancedString():
    s = insr()
    counter = collections.Counter(s)
    sorted_value = sorted(counter.values())

    if (sorted_value[-1] - sorted_value[0]) > 1:
        print('NO')
        return
    n = len(counter)

    if len(set(s[:n])) != n:
        print('NO')
        return

    for idx in range(n, len(s)):
        if s[idx] != s[idx%n]:
            print('NO')
            return

    print('YES')
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        aPerfectlyBalancedString()
