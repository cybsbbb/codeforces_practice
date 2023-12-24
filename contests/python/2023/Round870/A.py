import collections
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


def TrustNobody():
    n = inp()
    l = inlt()

    if max(l) == 0:
        print(0)
        return

    counter = collections.Counter(l)
    keys = sorted(counter.keys())
    counter_pre_sum = collections.defaultdict(int)
    counter_pre_sum[keys[0]] = counter[keys[0]]

    for key_idx in range(1, len(keys)):
        counter_pre_sum[keys[key_idx]] = counter_pre_sum[keys[key_idx-1]] + counter[keys[key_idx]]

    for key_idx in range(len(keys)-1):
        pre_sum = counter_pre_sum[keys[key_idx]]
        suf_sum = n - pre_sum
        if suf_sum >= keys[key_idx] and suf_sum < keys[key_idx+1]:
            print(suf_sum)
            return
    print(-1)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        TrustNobody()
