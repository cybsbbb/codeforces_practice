from collections import deque
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


class HopcroftKarp:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.graph = [[] for _ in range(n + 1)]
        self.match = [-1] * (n + m + 1)
        self.dist = [0] * (n + m + 1)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self):
        queue = deque()
        for u in range(1, self.n + 1):
            if self.match[u] == -1:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')

        self.dist[0] = float('inf')

        while queue:
            u = queue.popleft()
            if self.dist[u] < self.dist[0]:
                for v in self.graph[u]:
                    if self.dist[self.match[v]] == float('inf'):
                        self.dist[self.match[v]] = self.dist[u] + 1
                        queue.append(self.match[v])

        return self.dist[0] != float('inf')

    def dfs(self, u):
        if u != 0:
            for v in self.graph[u]:
                if self.dist[self.match[v]] == self.dist[u] + 1 and self.dfs(self.match[v]):
                    self.match[u] = v
                    self.match[v] = u
                    return True

            self.dist[u] = float('inf')
            return False

        return True

    def max_matching(self):
        matching = 0

        while self.bfs():
            for u in range(1, self.n + 1):
                if self.match[u] == -1 and self.dfs(u):
                    matching += 1

        return matching


# input the chess board
n, m = inlt()
board = []
for _ in range(n):
    board.append(insr())

# left (rows) segments idx
cur_idx = 0
r_idx = [[0] * m for i in range(n)]
for i in range(n):
    cur_idx += 1
    r_idx[i][0] = cur_idx
    for j in range(1, m):
        if board[i][j] != board[i][j-1] and board[i][j] == 'p':
            cur_idx += 1
        r_idx[i][j] = cur_idx
left_node_cnt = cur_idx

# right (columns) segments idx
cur_idx = 0
c_idx = [[0] * m for i in range(n)]
for j in range(m):
    cur_idx += 1
    c_idx[0][j] = cur_idx
    for i in range(1, n):
        if board[i][j] != board[i-1][j] and board[i][j] == 'p':
            cur_idx += 1
        c_idx[i][j] = cur_idx
right_node_cnt = cur_idx

# create the graph
hk = HopcroftKarp(left_node_cnt, right_node_cnt)

for i in range(n):
    for j in range(m):
        if board[i][j] == '-':
            hk.add_edge(r_idx[i][j], c_idx[i][j])

# HK algorithm
print(hk.max_matching())
