import sys

input = sys.stdin.readline


def inlt():
    return (list(map(int, input().split())))


if __name__ == '__main__':
    H, W, K = inlt()
    x1, y1, x2, y2 = inlt()

    # row, col, non, tar
    row = 0
    col = 0
    non = 0
    tar = 0
    pre_state = [0] * 4
    nxt_state = [0] * 4

    if x2 == x1 and y2 == y1:
        tar = 1
    elif x2 == x1:
        row = 1
    elif y2 == y1:
        col = 1
    else:
        non = 1

    for i in range(K):
        row_new = row * (W - 2) % 998244353 + non + tar * (W-1) % 998244353
        col_new = col * (H - 2) % 998244353 + non + tar * (H-1) % 998244353
        non_new = row * (H - 1) % 998244353 + col * (W - 1) % 998244353 + non * (W + H - 4) % 998244353
        tar_new = row + col
        row = row_new
        col = col_new
        non = non_new
        tar = tar_new

    print(tar % 998244353)
