from typing import List
import sys
import collections
sys.setrecursionlimit(500100)

# Meta Coding Puzzle:

# Python program to find strongly connected components in a given
# directed graph using Tarjan's algorithm (single DFS)
# Complexity : O(V+E)

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


def getMaxVisitableWebpages(N: int, M: int, A: List[int], B: List[int]) -> int:
    graph = collections.defaultdict(set)
    for Ai, Bi in zip(A, B):
        graph[Ai - 1].add(Bi - 1)

    tarjan = Tarjan(N, graph)
    tarjan.get_all_components()

    # map all node to components idx
    vertex_idx_to_component_idx = dict()
    for component_idx, vertex_idx_list in tarjan.components.items():
        for vertex_idx in vertex_idx_list:
            vertex_idx_to_component_idx[vertex_idx] = component_idx

    # replace components as node
    new_graph = collections.defaultdict(set)
    for vertex_from, vertex_to_set in graph.items():
        component_from = vertex_idx_to_component_idx[vertex_from]
        component_to_set = {vertex_idx_to_component_idx[vertex_to] for vertex_to in vertex_to_set}
        component_to_set.discard(component_from)
        new_graph[component_from].update(component_to_set)

    # topology sort
    indegrees = [0] * tarjan.component_idx
    for component_from, component_to_set in new_graph.items():
        for component_to in component_to_set:
            indegrees[component_to] += 1

    queue = collections.deque()
    for component_idx, indegree in enumerate(indegrees):
        if indegree == 0:
            queue.append(component_idx)

    longest_path = [len(tarjan.components[i]) for i in range(tarjan.component_idx)]

    while queue:
        cur_component = queue.popleft()
        for nxt_component in new_graph[cur_component]:
            longest_path[nxt_component] = max(longest_path[nxt_component], longest_path[cur_component] + len(tarjan.components[nxt_component]))
            indegrees[nxt_component] -= 1
            if indegrees[nxt_component] == 0:
                queue.append(nxt_component)

    return max(longest_path)


N = 10
M = 9
A = [3, 2, 5, 9, 10, 3, 3, 9, 4]
B = [9, 5, 7, 8, 6, 4, 5, 3, 9]
ans = getMaxVisitableWebpages(N, M, A, B)
print(ans)




