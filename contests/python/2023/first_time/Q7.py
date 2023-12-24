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

query_history = {}

def GuessKthZero(n, k):
    left = 1
    right = n
    while left < right:
        mid = left + (right - left) // 2
        if (left, mid) in query_history:
            respond = query_history[(left, mid)]
        else:
            print("? {} {}".format(left, mid))
            sys.stdout.flush()
            respond = inp()
            query_history[(left, mid)] = respond
        left0 = mid - left + 1 - respond
        if left0 < k:
            left = mid + 1
            k -= left0
        else:
            right = mid
        if (left, right) in query_history:
            query_history[(left, right)] += 1

    print("! {}".format(left))
    sys.stdout.flush()
    return


if __name__ == '__main__':
    n, t = inlt()
    for i in range(t):
        k = inp()
        GuessKthZero(n, k)
