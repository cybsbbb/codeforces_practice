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
    n = inp()
    trump = input()[:-1]
    card_sets = ['C', 'D', 'H', 'S']
    cards = input()[:-1].split()
    cnt = collections.defaultdict(list)
    for card in cards:
        card_set = card[1]
        cnt[card_set].append(card[0])

    for card_set in card_sets:
        cnt[card_set].sort()

    res = []
    trump_idx = 0
    for card_set in card_sets:
        if card_set == trump:
            continue
        for i in range(len(cnt[card_set]) // 2):
            res.append((cnt[card_set][2 * i] + card_set, cnt[card_set][2 * i + 1] + card_set))
        if len(cnt[card_set]) % 2 == 1:
            if trump_idx < len(cnt[trump]):
                res.append((cnt[card_set][-1] + card_set, cnt[trump][trump_idx] + trump))
                trump_idx += 1
            else:
                print("IMPOSSIBLE")
                return
    while trump_idx < len(cnt[trump]):
        res.append((cnt[trump][trump_idx] + trump, cnt[trump][trump_idx + 1] + trump))
        trump_idx += 2

    for round in res:
        print(*round)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
