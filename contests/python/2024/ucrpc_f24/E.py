import collections
import sys
import heapq
import math

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


n = inp()
point = [0, 0]
start = True
first_serve = 0
cur_serve = 0

for _ in range(n):
    score = inp()
    # check if start
    if start:
        start = False
        cur_serve = first_serve
    # get point
    if score == 1:
        point[cur_serve] += 1
    else:
        point[int(not cur_serve)] += 1
    print(f'{point[0]}:{point[1]}')
    # check win
    if max(point) > 10 and abs(point[0] - point[1]) > 1:
        if point[0] > point[1]:
            print('Player X wins the game.')
        else:
            print('Player Y wins the game.')
        start = True
        first_serve = int(not first_serve)
        point = [0, 0]
    # check server change
    if (point[0] + point[1]) >= 20:
        cur_serve = int(not cur_serve)
    else:
        if (point[0] + point[1]) % 2 == 0:
            cur_serve = int(not cur_serve)


