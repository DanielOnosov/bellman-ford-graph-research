def bellman_ford_matrix(matrix, n, start):
    dist = [float('inf')] * n
    dist[start] = 0
    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                if matrix[u][v] != float('inf') and dist[u] != float('inf') and dist[u] + matrix[u][v] < dist[v]:
                    dist[v] = dist[u] + matrix[u][v]
    for u in range(n):
        for v in range(n):
            if matrix[u][v] != float('inf') and dist[u] != float('inf') and dist[u] + matrix[u][v] < dist[v]:
                return "Negative cycle"
    return dist


def bellman_ford_list(graph, n, start):
    dist = [float('inf')] * n
    dist[start] = 0
    
    for i in range(n - 1):
        for u in range(len(graph)):
            for v, weight in graph[u]:
                if v < n and dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
    
    for u in range(len(graph)):
        for v, weight in graph[u]:
            if v < n and dist[u] != float('inf') and dist[u] + weight < dist[v]:
                return "Negative cycle"
    
    return dist


# n = 5
# inf = float('inf')
# matrix = [
#     [inf, 6,   inf, 7,   inf],
#     [inf, inf, 5,   8,   -4 ],
#     [inf, -2,  inf, inf, inf],
#     [inf, inf, -3,  inf, 9  ],
#     [2,   inf, 7,   inf, inf]
# ]
#
#
# graph_list = [
#     [(1, 6), (3, 7)],
#     [(2, 5), (3, 8), (4, -4)],
#     [(1, -2)],
#     [(2, -3), (4, 9)],
#     [(0, 2), (2, 7)]
# ]
#
# start = 0
# matrix_result = bellman_ford_matrix(matrix, n, start)
# print(matrix_result, "matrix")
#
# list_result = bellman_ford_list(graph_list, n, start)
# print(list_result, "list")
