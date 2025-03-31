from graph_matrix import GraphM
from graph_list import GraphList
from connectivity import Connectivity
def main():
    graph1N = 100
    graph1D = 0.1
    graph1Min = -20
    graph1Max = 20

    # connected = Connectivity()
    # graph = GraphM()
    #
    # matrix = graph.generate_matrix(graph1N, graph1D, graph1Min, graph1Max)
    #
    # graph.visualize(matrix, graph1N, graph1D)
    #
    # connected.Check(0, matrix)

    graph = GraphList()
    g = graph.generate(graph1N, graph1D, graph1Min, graph1Max)

    # graph.visualize(graph.transpose(g), graph1N, graph1D, "transposed")
    graph.visualize(g, graph1N, graph1D)
    graph.check_connectivity(g, graph1N)



main()
