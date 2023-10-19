import itertools
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


if __name__ == '__main__':
    N, M = inlt()
    graph_A = set()
    for i in range(M):
        graph_A.add(str(inlt()))

    cords_B = []
    for i in range(M):
        cords_B.append(inlt())

    out_flag = False
    for perm in itertools.permutations(range(N)):
        flag = True
        for a, b in cords_B:
            if str(sorted([perm[a-1]+1, perm[b-1]+1])) not in graph_A:
                flag = False
                break
        if flag is True:
            print("Yes")
            out_flag = True
            break

    if out_flag is False:
        print("No")
