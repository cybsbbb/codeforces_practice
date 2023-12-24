import collections
import sys
import math
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


def get_point_penalty(times, h):
    point = 0
    penalty = 0
    tmp_time = 0
    for ti in sorted(times):
        tmp_time += ti
        if tmp_time <= h:
            point += 1
            penalty += tmp_time
        else:
            break
    return point, penalty


def solution():
    n, m = inlt()
    symptoms = int(input()[:-1], 2)
    medicines = []
    for i in range(m):
        days = inp()
        removes = int(input()[:-1], 2)
        sides = int(input()[:-1], 2)
        medicines.append([days, removes, sides])
    # No medicine needed
    if symptoms == 0:
        print("0")
        return

    states = [float('inf')] * 1024
    states[symptoms] = 0

    q = []
    heapq.heappush(q, (0, symptoms))
    while len(q) > 0:
        cur_days, symptoms = heapq.heappop(q)
        if symptoms == 0:
            print(cur_days)
            return
        for days, removes, sides in medicines:
            nxt_days = cur_days + days
            nxt_symptoms = symptoms & (~removes) | sides
            if states[nxt_symptoms] > nxt_days:
                states[nxt_symptoms] = nxt_days
                heapq.heappush(q, (nxt_days, nxt_symptoms))

    print("-1")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
