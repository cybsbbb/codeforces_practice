import sys
from collections import defaultdict, deque
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


def solution():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = sorted(zip(a, b), key=lambda x: -x[0])
    cnt = [0] * (n + 1)
    ans = 0
    i = 1
    while i * i <= 2 * n:
        for j in range(n + 1):
            cnt[j] = 0
        for x, y in c:
            count = i * x - y

            if x == i:
                ans += cnt[y]
            if 0 <= count <= n:
                cnt[count] += 1

        i += 1

    print(ans)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
