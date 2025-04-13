import csv
import time

from numpy.ma.extras import average

import data_geneartor
from bellman_ford import bellman_ford_matrix, bellman_ford_list
from graph_matrix import GraphM
from graph_list import GraphList
from connectivity import Connectivity


def main():


    matrixes = data_geneartor.data_geneartor("2", 200)
    data_geneartor.get_time(2, matrixes, "../Responses_Analyzer/matrixes_200.csv")

    lists = data_geneartor.data_geneartor("1", 200)
    data_geneartor.get_time("1", lists, "../Responses_Analyzer/lists_200.csv")

    # data = []
    # graph1N = 1
    # graph1D = 0.00
    # graph1Min = -10
    # graph1Max = -1
    #
    # graph = GraphList()
    #
    # for j in range(0, 20):
    #     graph1N = 1
    #     times = []
    #     graph1D = graph1D + 0.05
    #
    #     for i in range(0, 1001):
    #         if (i % 10 == 0 and i != 0):
    #             avg_time = average(times)
    #             data.append({"Number of vertices": graph1N, "density": graph1D, "time": avg_time})
    #             if (i == 1000):
    #                 break
    #             times = []
    #             graph1N = graph1N + 1
    #
    #         matrix = graph.generate(graph1N, graph1D, graph1Min, graph1Max)
    #
    #         #graph.visualize(matrix, graph1N, graph1D)
    #
    #         #graph.check_connectivity(matrix, graph1N)
    #
    #         start = time.perf_counter()
    #         dist = bellman_ford_list(matrix, graph1N, 0)
    #         end = time.perf_counter()
    #         times.append((end - start)*1000)
    #         print(graph1N, " ",graph1D, " ", (end-start)*1000)
    #
    # with open("../Responses_Analyzer/data_list.csv", mode="w", newline="") as file:
    #     fieldnames = ["Number of vertices", "density", "time"]
    #     writer = csv.DictWriter(file, fieldnames=fieldnames)
    #
    #     writer.writeheader()
    #     writer.writerows(data)


    # graph = GraphList()
    # g = graph.generate(graph1N, graph1D, graph1Min, graph1Max)
    #
    # # graph.visualize(graph.transpose(g), graph1N, graph1D, "transposed")
    # graph.visualize(g, graph1N, graph1D)
    # graph.check_connectivity(g, graph1N)
    # dist = bellman_ford_list(g, graph1N,0)
    # print(dist)


main()


