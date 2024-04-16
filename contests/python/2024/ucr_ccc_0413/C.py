import sys

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


for _ in range(1):
    h, w, n = inlt()
    t = input()[:-1]
    map = []
    for i in range(h):
        map.append(input()[:-1])

    ans = 0
    for i in range(h):
        for j in range(w):
            if map[i][j] == '.':
                flag = True
                cur_i, cur_j = i, j
                for d in t:
                    if d == 'U':
                        cur_i -= 1
                    elif d == 'D':
                        cur_i += 1
                    elif d == 'L':
                        cur_j -= 1
                    elif d == 'R':
                        cur_j += 1
                    if not map[cur_i][cur_j] == '.':
                        flag = False
                        break
                ans += 1 if flag else 0
    print(ans)
