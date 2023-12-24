import collections
import bisect
import sys
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


def position(piece):
    return ord(piece[0])-ord('a'), ord(piece[1])-ord('1')


if __name__ == '__main__':
    moves = [[2, 1], [1, 2], [-2, 1], [-1, 2], [2, -1], [1, -2], [-2, -1], [-1, -2]]
    board_idx = 0
    while(1):
        board_idx += 1
        n = inp()
        if n == -1:
            break
        else:
            # Init Board
            pieces = input().split()
            start, des = input().split()
            seen = set()
            for piece in pieces:
                pos = position(piece)
                seen.add(str(pos))
            # Init vars
            pos_start = position(start)
            pos_des = position(des)
            cur_layer = [pos_start]
            step = 0
            flag = False
            while len(cur_layer) > 0:
                if flag is True: break
                step += 1
                nxt_layer = []
                for pos in cur_layer:
                    if flag is True: break
                    for move in moves:
                        if flag is True: break
                        nxt_pos = (pos[0]+move[0], pos[1]+move[1])
                        if 0 <= nxt_pos[0] <= 7 and 0 <= nxt_pos[1] <= 7:
                            if nxt_pos[0] == pos_des[0] and nxt_pos[1] == pos_des[1]:
                                flag = True
                                break
                            else:
                                if str(nxt_pos) not in seen:
                                    seen.add(str(nxt_pos))
                                    nxt_layer.append(nxt_pos)
                        else:
                            continue
                cur_layer = nxt_layer
            if flag:
                print(f"Board {board_idx}: {step} moves")
            else:
                print(f"Board {board_idx}: not reachable")

