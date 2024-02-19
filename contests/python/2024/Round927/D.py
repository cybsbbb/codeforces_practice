
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
    n = inlt()
    trump = input()[:-1]
    cards = input().split()
    stat = collections.defaultdict(list)
    suits = ['C', 'D', 'H', 'S']
    for card in cards:
        card_number = card[0]
        card_suit = card[1]
        stat[card_suit].append(card_number)

    for suit in suits:
        stat[suit].sort()

    ans = []
    flag = True
    for suit in suits:
        if suit != trump:
            for i in range(len(stat[suit]) // 2):
                ans.append((str(stat[suit][2*i]) + suit, str(stat[suit][2*i+1]) + suit))
            if len(stat[suit]) % 2 == 1:
                if len(stat[trump]) > 0:
                    ans.append((str(stat[suit][-1]) + suit, str(stat[trump].pop()) + trump))
                else:
                    flag = False
                    break
    if flag is False:
        print("IMPOSSIBLE")
        return
    else:
        for i in range(len(stat[trump]) // 2):
            ans.append((str(stat[trump][2 * i]) + trump, str(stat[trump][2 * i + 1]) + trump))

    for pair in ans:
        print(*pair)

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
