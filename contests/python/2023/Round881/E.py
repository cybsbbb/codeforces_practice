import sys
sys.setrecursionlimit(200000)

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
    n, m = inlt()
    boundaries = []
    for i in range(m):
        boundaries.append(inlt())
    q = inp()
    changes = []
    for i in range(q):
        changes.append(inp())




if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
