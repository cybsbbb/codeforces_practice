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


def SubtleSubstringSubtraction():
    s = insr()

    alice = 0
    bob = 0

    if len(s) % 2 == 0:
        for c in s:
            alice += (ord(c) - ord('a') + 1)
        print(f"Alice {alice}")
        return
    else:
        if s[0] >= s[-1]:
            for c in s[:-1]:
                alice += (ord(c) - ord('a') + 1)
            bob = ord(s[-1]) - ord('a') + 1
        else:
            for c in s[1:]:
                alice += (ord(c) - ord('a') + 1)
            bob = ord(s[0]) - ord('a') + 1

        if alice > bob:
            print(f"Alice {alice-bob}")
        else:
            print(f"Bob {bob-alice}")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        SubtleSubstringSubtraction()
