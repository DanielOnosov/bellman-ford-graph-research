from collections import deque
from graph_matrix import GraphM


class Connectivity:
    def __init__(self):
        pass

    def Check(self, start, matrix):
        len1 = self.DFS(start, matrix)

        ghelper = GraphM()
        transposedMatrix = ghelper.transpose(matrix)

        len2 = self.DFS(start, transposedMatrix)

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
                    if matrix[node][neighbor_id] and neighbor_id not in visited:
                        stack.append(neighbor_id)

        print(f"Visited: {len(visited)}")
        return len(visited)