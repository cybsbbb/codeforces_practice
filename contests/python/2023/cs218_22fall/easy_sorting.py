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


if __name__ == '__main__':
    t = inp()
    candies = []
    for i in range(t):
        candies.append(inp())

    res = 0
    cnt = collections.Counter(candies)
    cnt13 = 0
    cnt31 = 0
    for i in range(cnt[1]):
        if candies[i] == 3:
            cnt13 += 1
    for i in range(cnt[1], cnt[1] + cnt[2]):
        if candies[i] != 2:
            res += 1
    for i in range(cnt[1] + cnt[2], cnt[1] + cnt[2] + cnt[3]):
        if candies[i] == 1:
            cnt31 += 1
    res += (cnt13 + cnt31) - min(cnt13, cnt31)
    print(res)
