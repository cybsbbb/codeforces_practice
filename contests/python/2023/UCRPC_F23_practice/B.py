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
    yes = 0
    noop = 0
    sheldon = None
    for i in range(4):
        s = input()[:-1]
        name, vote = s.split(': ')
        if vote == 'yes':
            yes += 1
        else:
            noop += 1
        if name == 'Sheldon':
            sheldon = vote

    if yes > noop:
        print('yes')
    elif noop > yes:
        print('no')
    else:
        print(sheldon)

    return


if __name__ == '__main__':
    # t = inp()
    for i in range(1):
        solution()
