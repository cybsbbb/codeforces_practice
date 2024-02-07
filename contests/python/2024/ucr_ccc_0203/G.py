import bisect
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


class Tarjan:
    def __init__(self, V, graph):
        # Number of the vertex
        self.V = V
        # Edges of the graph, dictionary of set/list
        self.graph = graph
        # Timestamp during dfs
        self.timestamp = 0
        # vertex timestamp
        self.vertex_time = [-1] * self.V
        # lowest link for each vertex
        self.vertex_lowlink = [-1] * self.V
        # Stack member (quick check if in stack)
        self.stack_member = [False] * self.V
        # current Stack
        self.stack = []
        # Result SCC
        self.components = dict()
        # scc index
        self.component_idx = 0

    def get_all_components(self):
        for i in range(self.V):
            if self.vertex_time[i] == -1:
                self.get_components(i)

    def get_components(self, cur_vertex):
        self.vertex_time[cur_vertex] = self.timestamp
        self.vertex_lowlink[cur_vertex] = self.timestamp
        self.timestamp += 1
        self.stack_member[cur_vertex] = True
        self.stack.append(cur_vertex)

        for nxt_vertex in self.graph[cur_vertex]:
            if self.vertex_time[nxt_vertex] == -1:
                self.get_components(nxt_vertex)
                self.vertex_lowlink[cur_vertex] = min(self.vertex_lowlink[cur_vertex], self.vertex_lowlink[nxt_vertex])
            elif self.stack_member[nxt_vertex] == True:
                self.vertex_lowlink[cur_vertex] = min(self.vertex_lowlink[cur_vertex], self.vertex_time[nxt_vertex])

        stack_top_vertex = -1
        if self.vertex_lowlink[cur_vertex] == self.vertex_time[cur_vertex]:
            component = []
            while stack_top_vertex != cur_vertex:
                stack_top_vertex = self.stack.pop()
                component.append(stack_top_vertex)
                self.stack_member[stack_top_vertex] = False
            self.components[self.component_idx] = component
            self.component_idx += 1


def solution():
    h, w = inlt()
    grid = []

    n = h * w
    for _ in range(h):
        grid.append(insr())
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    graph = collections.defaultdict(set)

    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                for di, dj in directions:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < h and 0 <= jj < w and grid[ii][jj] == '#':
                        graph[ii * w + jj].add(i * w + j)
                        graph[i * w + j].add(ii * w + jj)
    V = len(graph)
    old_vertex = list(graph.keys())
    new_vertex = range(V)

    map_forward = dict(zip(range(V), graph.keys()))
    map_backward = dict(graph.keys(), zip(range(V)))



if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
