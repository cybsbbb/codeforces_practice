import sys
import heapq
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
    n = inp()
    a = []
    b = []
    for i in range(n):
        a_i, b_i = inlt()
        a.append(a_i)
        b.append(b_i)
    ab = list(zip(a, b))
    ab.sort(key=lambda X:(X[0], -X[1]))

    heap = []
    on = 0
    eliminated = 0
    res = 0

    for i in range(n):
        a, b = ab[i]
        if a <= eliminated:
            continue
        else:
            res += b
            on += 1
            heapq.heappush(heap, a)

        if on >= heap[0]:
            tmp_on = on
            while len(heap) > 0 and heap[0] <= tmp_on:
                eliminated = heapq.heappop(heap)
                on -= 1
    print(res)
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
