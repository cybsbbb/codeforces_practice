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
    game = []
    for i in range(3):
        game.append(insr())

    for i in range(3):
        if game[i][0] == game[i][1] and game[i][1] == game[i][2] and game[i][1] != '.':
            print(game[i][1])
            return
        if game[0][i] == game[1][i] and game[1][i] == game[2][i] and game[1][i] != '.':
            print(game[1][i])
            return
    if game[0][0] == game[1][1] and game[1][1] == game[2][2] and game[1][1] != '.':
        print(game[1][1])
        return
    if game[0][2] == game[1][1] and game[1][1] == game[2][0] and game[1][1] != '.':
        print(game[1][1])
        return
    print("DRAW")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
