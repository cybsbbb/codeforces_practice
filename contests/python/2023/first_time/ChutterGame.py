import sys
import math
import collections
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


def ChutterGame(n, lst):
    pre_map = collections.defaultdict(list)
    for curr_idx in range(n-1):
        for nxt_step in range(1, 7):
            nxt_idx = (curr_idx + nxt_step)%n
            pre_map[(nxt_idx + lst[nxt_idx])%n].append(curr_idx)

    if len(pre_map[n-1]) == 0:
        print("{:.3f}".format(0))
        return

    curr_prob = [0] * n
    next_prob = [0] * n
    curr_prob[0] = 1
    res = 0
    for iter in range(1, 150000):
        for idx in range(n):
            next_prob[idx] = sum(curr_prob[pre_idx] for pre_idx in pre_map[idx]) / 6
        curr_prob, next_prob = next_prob, curr_prob
        res += iter * curr_prob[n - 1]
    print("{:.3f}".format(math.ceil(res*10000)/10000))


if __name__ == '__main__':
    n = inp()
    lst = inlt()
    ChutterGame(n, lst)
