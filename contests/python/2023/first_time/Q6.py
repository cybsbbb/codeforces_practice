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


def GuessKthZero(n):
    k = inp()
    left = 1
    right = n
    while left < right:
        mid = left + (right - left) // 2
        print("? {} {}".format(left, mid))
        sys.stdout.flush()

        respond = inp()
        left0 = mid - left + 1 - respond
        if left0 < k:
            left = mid + 1
            k -= left0
        else:
            right = mid

    print("! {}".format(left))
    sys.stdout.flush()
    return


if __name__ == '__main__':
    n, t = inlt()
    GuessKthZero(n)
