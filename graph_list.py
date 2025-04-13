import random
import graphviz
from utils import *


class GraphList:
    def generate(self, n, p, min, max):
        graph = []

        #checkConnectivity(n, p)

        numOfEdges = 0

        for i in range(n):
            graph.append([])  # init all vertexes
            for j in range(n):
                if i == j:
                    continue

                randomValue = random.uniform(0, 1)

                if (i == 0 and j == 0) or randomValue <= p:
                    weight = random.randint(min, max)

                    numOfEdges += 1
                    graph[i].append((weight, j))

        #print(f"Number of edges: {numOfEdges}")

        return graph

    def visualize(self, graph, n, density):
        no_edge = float('inf')

        dot = graphviz.Digraph(comment=f"Nodes {n}. Density {density * 100}%", engine='sfdp')

        dot.attr(overlap="scale")
        dot.attr('edge', color="#00000040", penwidth="0.8")

        n = len(graph)
        for i in range(n):
            dot.node(str(i))

            for j in range(len(graph[i])):
                aij = graph[i][j]

                if aij != no_edge:
                    dot.edge(str(i), str(aij[1]), label=str(aij[0]))

        dot.render(f"output/{n}-{density}", format='png')

    def check_connectivity(self, graph, n):
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                aij = graph[i][j]

                count = self.DFS(aij, graph)

                if count != n:
                    print("Not fully connected")
                    return False

        print("Fully connected")
        return True

    def DFS(self, start, graph):
        visited = set()
        stack = [start]

        while stack:
            (w, node) = stack.pop()
            if node not in visited:
                visited.add(node)
                for (_, neighbor_id) in graph[node]:
                    if neighbor_id not in visited:
                        stack.append((_, neighbor_id))

        return len(visited)
