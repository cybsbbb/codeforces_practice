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
    n = inp()
    intervals = []
    for i in range(n):
        start, end = inlt()
        intervals.append((start, end))
    intervals.sort(key=lambda x: (x[1], -x[0]))

    res = 0
    nxt_interval = []
    pre_end = -1
    pre_intersection_end = -1
    for start, end in intervals:
        if start > pre_end:
            res += 1
            pre_end = end
        elif start <= pre_intersection_end:
            continue
        else:
            res += 1
            pre_intersection_end = pre_end
            pre_end = end
    print(res)
