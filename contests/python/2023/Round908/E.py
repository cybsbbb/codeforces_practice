import collections
import sys
import heapq

input = sys.stdin.readline


def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))
def insr():
    s = input()
    return (list(s[:len(s) - 1]))
def invr():
    return (map(int, input().split()))


def solution():
    m = inp()

    sml = 0
    smr = 0
    mst = collections.defaultdict(list)

    for i in range(m):
        n, l, r = inlt()
        sml += l
        smr += r
        a = inlt()
        c = inlt()
        smc = sum(c)

        for i, x in enumerate(a):
            mst[x].append((c[i], smc - c[i], l, r))

    ans = 10 ** 18

    for k in range(sml, smr + 1):
        if k not in mst:
            ans = 0
            break
        else:
            candidate = 0
            tot = smr
            for c, rm, l, r in mst[k]:
                tot -= r
                free = min(rm, r)
                tot += max(l, free)
                candidate += max(0, l - free)
            candidate += max(0, k - tot)
            ans = min(ans, candidate)
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
