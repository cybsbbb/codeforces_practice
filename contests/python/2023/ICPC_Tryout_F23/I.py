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
    map = []
    for _ in range(4):
        map.append(inlt())
    map_int = 0
    for i in range(4):
        for j in range(4):
            if map[i][j] == 1:
                map_int |= 1 << (i * 4 + j)

    res = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for candidate in range(1 << 16):
        if candidate & map_int != map_int:
            continue
        else:
            flag = True
            # Check if 1 is connected
            for i in range(16):
                if candidate & (1 << i):
                    x, y = i // 4, i % 4
                    seen = 1 << i
                    stack = collections.deque()
                    stack.append((x, y))
                    while stack:
                        xx, yy = stack.popleft()
                        for dx, dy in directions:
                            if 0 <= xx + dx < 4 and 0 <= yy + dy < 4 and \
                                    (candidate & (1 << ((xx + dx) * 4 + yy + dy))) and \
                                    (not seen & (1 << ((xx + dx) * 4 + yy + dy))):
                                stack.append((xx + dx, yy + dy))
                                seen |= (1 << ((xx + dx) * 4 + yy + dy))
                    if seen != candidate:
                        flag = False
                    break

            if flag is False:
                continue

            # Check if 0 is connected
            for x, y in [(1, 1), (1, 2), (2, 1), (2, 2)]:
                i = x * 4 + y
                if not candidate & (1 << i):
                    flag = False
                    seen = 1 << i
                    stack = collections.deque()
                    stack.append((x, y))
                    while stack:
                        xx, yy = stack.popleft()
                        for dx, dy in directions:
                            if 0 <= xx + dx < 4 and 0 <= yy + dy < 4 and (not candidate & (1 << ((xx + dx) * 4 + yy + dy))) and (not seen & (1 << ((xx + dx) * 4 + yy + dy))):
                                if xx + dx == 0 or xx + dx == 3 or yy + dy == 0 or yy + dy == 3:
                                    flag = True
                                    break
                                else:
                                    stack.append((xx + dx, yy + dy))
                                    seen |= (1 << ((xx + dx) * 4 + yy + dy))
                    if flag is False:
                        break

            if flag:
                res += 1

    print(res)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
