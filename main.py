from bellman_ford import bellman_ford_matrix, bellman_ford_list
from graph_matrix import GraphM
from graph_list import GraphList
from connectivity import Connectivity
def main():
    graph1N = 200
    graph1D = 0.01
    graph1Min = -20
    graph1Max = 20

    connected = Connectivity()
    graph = GraphM()

    matrix = graph.generate(graph1N, graph1D, graph1Min, graph1Max)

    graph.visualize(matrix, graph1N, graph1D)

    graph.check_connectivity(matrix, graph1N)

    dist = bellman_ford_matrix(matrix, graph1N,0)
    print(dist)

    # graph = GraphList()
    # g = graph.generate(graph1N, graph1D, graph1Min, graph1Max)
    #
    # # graph.visualize(graph.transpose(g), graph1N, graph1D, "transposed")
    # graph.visualize(g, graph1N, graph1D)
    # graph.check_connectivity(g, graph1N)
    # dist = bellman_ford_list(g, 0)



main()
