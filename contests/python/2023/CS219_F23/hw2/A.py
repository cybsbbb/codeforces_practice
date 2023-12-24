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

INF = 2147483647
NIL = 0

class BipGraph(object):
    # Constructor
    def __init__(self, m, n):
        # m and n are number of vertices on left
        # and right sides of Bipartite Graph
        self.__m = m
        self.__n = n
        # adj[u] stores adjacents of left side
        # vertex 'u'. The value of u ranges from 1 to m.
        # 0 is used for dummy vertex
        self.__adj = [[] for _ in range(m + 1)]

    # To add edge from u to v and v to u
    def addEdge(self, u, v):
        self.__adj[u].append(v)  # Add u to v’s list.

    # Returns true if there is an augmenting path, else returns
    # false
    def bfs(self):
        Q = deque()
        # First layer of vertices (set distance as 0)
        for u in range(1, self.__m + 1):
            # If this is a free vertex, add it to queue
            if self.__pairU[u] == NIL:
                # u is not matched3
                self.__dist[u] = 0
                Q.append(u)
            # Else set distance as infinite so that this vertex
            # is considered next time
            else:
                self.__dist[u] = INF
        # Initialize distance to NIL as infinite
        self.__dist[NIL] = INF
        # Q is going to contain vertices of left side only.
        while Q:
            # Dequeue a vertex
            u = Q.popleft()
            # If this node is not NIL and can provide a shorter path to NIL
            if self.__dist[u] < self.__dist[NIL]:
                # Get all adjacent vertices of the dequeued vertex u
                for v in self.__adj[u]:
                    # If pair of v is not considered so far
                    # (v, pairV[V]) is not yet explored edge.
                    if self.__dist[self.__pairV[v]] == INF:
                        # Consider the pair and add it to queue
                        self.__dist[self.__pairV[v]] = self.__dist[u] + 1
                        Q.append(self.__pairV[v])
        # If we could come back to NIL using alternating path of distinct
        # vertices then there is an augmenting path
        return self.__dist[NIL] != INF

    # Returns true if there is an augmenting path beginning with free vertex u
    def dfs(self, u):
        if u != NIL:
            # Get all adjacent vertices of the dequeued vertex u
            for v in self.__adj[u]:
                if self.__dist[self.__pairV[v]] == self.__dist[u] + 1:
                    # If dfs for pair of v also returns true
                    if self.dfs(self.__pairV[v]):
                        self.__pairV[v] = u
                        self.__pairU[u] = v
                        return True
            # If there is no augmenting path beginning with u.
            self.__dist[u] = INF
            return False
        return True

    def hopcroftKarp(self):
        # pairU[u] stores pair of u in matching where u
        # is a vertex on left side of Bipartite Graph.
        # If u doesn't have any pair, then pairU[u] is NIL
        self.__pairU = [0 for _ in range(self.__m + 1)]

        # pairV[v] stores pair of v in matching. If v
        # doesn't have any pair, then pairU[v] is NIL
        self.__pairV = [0 for _ in range(self.__n + 1)]

        # dist[u] stores distance of left side vertices
        # dist[u] is one more than dist[u'] if u is next
        # to u'in augmenting path
        self.__dist = [0 for _ in range(self.__m + 1)]
        # Initialize result
        result = 0

        # Keep updating the result while there is an
        # augmenting path.
        while self.bfs():
            # Find a free vertex
            for u in range(1, self.__m + 1):
                # If current vertex is free and there is
                # an augmenting path from current vertex
                if self.__pairU[u] == NIL and self.dfs(u):
                    result += 1
        return result


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


g = BipGraph(left_node_cnt, right_node_cnt)

for i in range(n):
    for j in range(m):
        if board[i][j] == '-':
            left_node = r_idx[i][j]
            right_node = c_idx[i][j]
            g.addEdge(left_node, right_node)

print(g.hopcroftKarp())
