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


def allZeroSequence():
    n = inp()
    s = inlt()

    s_counter = collections.Counter(s)

    if 0 in s_counter:
        print(n - s_counter[0])
        return
    else:
        for key in s_counter:
            if s_counter[key] >= 2:
                print(n)
                return

        print(n+1)
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        allZeroSequence()
