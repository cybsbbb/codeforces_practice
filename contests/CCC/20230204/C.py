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


def class_field_trip(ann, ben):
    res = []
    n = len(ann)
    m = len(ben)
    idx_a = 0
    idx_b = 0
    while idx_a < n and idx_b < m:
        if ann[idx_a] <= ben[idx_b]:
            res.append(ann[idx_a])
            idx_a += 1
        else:
            res.append(ben[idx_b])
            idx_b += 1

    if idx_a == n:
        for i in range(idx_b, m):
            res.append(ben[i])
    elif idx_b == m:
        for i in range(idx_a, n):
            res.append(ann[i])
    print(''.join(res))
    return 0


if __name__ == '__main__':
    ann = insr()
    ben = insr()
    class_field_trip(ann, ben)
