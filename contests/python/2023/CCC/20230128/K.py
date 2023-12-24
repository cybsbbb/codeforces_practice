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


def relocation(N, Q):
    init_location = inlt()
    companies = collections.defaultdict(int)
    for i in range(1, N+1):
        companies[i] = init_location[i-1]
    for i in range(Q):
        q_type, p1, p2 = inlt()
        if q_type == 1:
            companies[p1] = p2
        if q_type == 2:
            print(abs(companies[p1] - companies[p2]))
    return 0


if __name__ == '__main__':
    N, Q = inlt()
    relocation(N, Q)
