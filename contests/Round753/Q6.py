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


def robotOnTheBoard2():
    input()
    n, m = inlt()
    board = []
    for i in range(n):
        board.append(insr())

    nxt_index = [-1] * (m * n)
    in_degree = [0] * (m * n)
    visited = [False] * (m * n)
    values = [0] * (m * n)

    for i in range(n):
        for j in range(m):
            index = i * m + j
            nxt_i = i
            nxt_j = j
            if board[i][j] == 'L':
                nxt_j -= 1
            elif board[i][j] == 'R':
                nxt_j += 1
            elif board[i][j] == 'U':
                nxt_i -= 1
            elif board[i][j] == 'D':
                nxt_i += 1
            if nxt_i < 0 or nxt_i >= n or nxt_j < 0 or nxt_j >= m:
                continue
            nxt_index[index] = nxt_i * m + nxt_j
            in_degree[nxt_i * m + nxt_j] += 1

    for index in range(m*n):
        if in_degree[index] != 0:
            continue
        seq = []
        while not visited[index] and index != -1:
            seq.append(index)
            visited[index] = True
            index = nxt_index[index]

        # if this way out to the board
        if index == -1:
            for i, idx in enumerate(seq):
                values[idx] = len(seq) - i
        # encounter with other or looped
        else:
            base = values[index]
            loop_flag = False
            loop_length = len(seq)
            for i, idx in enumerate(seq):
                if idx == index:
                    loop_flag = True
                if loop_flag is False:
                    loop_length -= 1
                values[idx] = max(len(seq) - i, loop_length) + base

    # Handle the loops
    for index in range(m*n):
        if values[index] > 0:
            continue
        loop_length = 0
        seq = []
        while not visited[index]:
            seq.append(index)
            visited[index] = True
            index = nxt_index[index]
            loop_length += 1

        for idx in seq:
            values[idx] = loop_length

    maximum = max(values)
    for i in range(m * n):
        if values[i] == maximum:
            print(i // m + 1, i % m + 1, values[i])
            return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        robotOnTheBoard2()

