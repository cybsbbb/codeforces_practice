from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

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

# Python program to find strongly connected components in a given
# directed graph using Tarjan's algorithm (single DFS)
# Complexity : O(V+E)

# This class represents an directed graph
# using adjacency list representation

class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        self.Time = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


    def SCCUtil(self, u, low, disc, stackMember, st):

        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        stackMember[u] = True
        st.append(u)

        # Go through all vertices adjacent to this
        for v in self.graph[u]:

            # If v is not visited yet, then recur for it
            if disc[v] == -1:

                self.SCCUtil(v, low, disc, stackMember, st)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                # Case 1 (per above discussion on Disc and Low value)
                low[u] = min(low[u], low[v])

            elif stackMember[v] == True:
                low[u] = min(low[u], disc[v])

        # head node found, pop the stack and print an SCC
        w = -1  # To store stack extracted vertices
        if low[u] == disc[u]:
            component = []
            while w != u:
                w = st.pop()
                component.append(w)
                stackMember[w] = False
            components.append(component)

    # The function to do DFS traversal.
    # It uses recursive SCCUtil()

    def SCC(self):

        # Mark all the vertices as not visited
        # and Initialize parent and visited,
        # and ap(articulation point) arrays
        disc = [-1] * (self.V)
        low = [-1] * (self.V)
        stackMember = [False] * (self.V)
        st = []

        # Call the recursive helper function
        # to find articulation points
        # in DFS tree rooted with vertex 'i'
        for i in range(self.V):
            if disc[i] == -1:
                self.SCCUtil(i, low, disc, stackMember, st)


n = inp()
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    k_list = inlt()
    for ki in k_list[1:]:
        graph[i].append(ki)

original_matching = [0] + inlt()
reverse_matching = [0] * (n + 1)
for i in range(1, n + 1):
    reverse_matching[original_matching[i]] = i

g = Graph(n + 1)
for i in range(1, n + 1):
    for j in graph[i]:
        g.addEdge(i, reverse_matching[j])

components = []
g.SCC()

component_cnt = len(components)
component_map = dict()

for i in range(component_cnt):
    for node in components[i]:
        component_map[node] = i

res = [[] for _ in range(n+1)]

for i in range(1, n + 1):
    for j in graph[i]:
        if component_map[i] == component_map[reverse_matching[j]]:
            res[i].append(j)

for i in range(1, n + 1):
    print(len(res[i]), end=' ')
    print(*sorted(res[i]))

