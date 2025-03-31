import random
import graphviz
from utils import *

class GraphM:
    no_edge = float('inf')

    def create_empty_matrix(self, n):
        matrix = []

        for i in range(n):
            matrix.append([])
            for j in range(n):
                matrix[i].append(0)

        return matrix

    def generate(self, n, p, min, max):
        matrix = []

        checkConnectivity(n, p)

        numOfEdges = 0

        for i in range(n):
            matrix.append([])
            for j in range(n):
                randomValue = random.uniform(0, 1)

                if randomValue > p:
                    matrix[i].append(self.no_edge)
                else:
                    weight = random.randint(min, max)

                    numOfEdges += 1
                    matrix[i].append(weight)

        print(f"Number of edges: {numOfEdges}")

        return matrix

    def transpose(self, matrix):
        newMatrix = []
        n = len(matrix)

        for i in range(n):
            newMatrix.append([])
            for j in range(n):
                newMatrix[i].append(matrix[j][i])

        return newMatrix

    def visualize(self, matrix, n, density, prefix=""):
        dot = graphviz.Digraph(comment=f"Nodes {n}. Density {density * 100}%", engine='sfdp')

        dot.attr(overlap="scale")
        dot.attr('edge', color="#00000040", penwidth="0.8")

        n = len(matrix)
        for i in range(n):
            dot.node(str(i))

            for j in range(n):
                aij = matrix[i][j]

                if aij != self.no_edge:
                    dot.edge(str(i), str(j), label=str(aij))

        dot.render(f"output/{prefix}_{n}-{density}", format='png')

    def check_connectivity(self, matrix, n):
        len1 = self.DFS(0, matrix)

        transposedMatrix = self.transpose(matrix)

        len2 = self.DFS(0, transposedMatrix)

        numberOfNodes = len(matrix)

        if numberOfNodes == len2 and numberOfNodes == len1:
            print("Fully connected")
        else:
            print("Not fully connected")

    def DFS(self, start, matrix):

        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor_id in range(len(matrix[node])):
                    if matrix[node][neighbor_id] != self.no_edge and neighbor_id not in visited:
                        stack.append(neighbor_id)

        print(f"Visited: {len(visited)}")
        return len(visited)
