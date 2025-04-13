import csv
import math
import random
import time

from numpy.ma.extras import average

import bellman_ford
from graph_list import GraphList
from graph_matrix import GraphM


def data_geneartor(type, num_vertexes, min_weight, max_weight, repetitions):
    graphs = []
    densities = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]

    if type == "1":
        graph_geneartor = GraphList()

    elif type == "2":
        graph_geneartor = GraphM()

    for i in range(20):
        density = densities[i]
        vertexes = 0
        for j in range(num_vertexes):
            vertexes = vertexes + 1
            for k in range(repetitions):
                graphs.append((graph_geneartor.generate(vertexes, density, min_weight, max_weight), vertexes, density))
                #print(k," ","vertexes: {}, density: {}".format(vertexes, density))

    return graphs

def get_time(type, graphs, repetitions,file_path):

    to_write = []
    times = []
    if type == "1":
        for graph in graphs:
            start_vertex = random.randint(0, graph[1]-1)

            start = time.perf_counter()
            bellman_ford.bellman_ford_list(graph[0], graph[1], start_vertex)
            end = time.perf_counter()

            times.append((end - start) * 1000)
            if (len(times) == repetitions):
                to_write.append({"vertexes": graph[1],"density": graph[2] ,"time": average(times)})
                times = []

            #print(graph[1], " ", graph[2], " ", (end - start) * 1000)
    else:
        for graph in graphs:
            start_vertex = random.randint(0, graph[1]-1)


            start = time.perf_counter()
            bellman_ford.bellman_ford_matrix(graph[0], graph[1], start_vertex)
            end = time.perf_counter()

            times.append((end - start) * 1000)
            if (len(times) == repetitions):
                to_write.append({"vertexes": graph[1],"density": graph[2] ,"time": average(times)})
                times = []

            #print(graph[1], " ", graph[2], " ", (end - start) * 1000)


    with open(file_path, mode="a", newline="") as file:
        fieldnames = ["vertexes", "density", "time"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(to_write)

def get_time_prob(type, graphs, repetitions, probability, file_path):

    to_write = []
    times = []
    outcomes = []
    if type == "1":
        for graph in graphs:
            start_vertex = random.randint(0, graph[1]-1)

            start = time.perf_counter()
            result = bellman_ford.bellman_ford_list(graph[0], graph[1], start_vertex)
            end = time.perf_counter()

            if result == 1:
                outcomes.append(result)
            else:
                outcomes.append(0)

            times.append((end - start) * 1000)
            if (len(times) == repetitions):
                to_write.append({"vertexes": graph[1],"density": graph[2] ,"time": average(times), "probability": probability, "result": sum(outcomes)/len(outcomes)})
                times = []

            #print(graph[1], " ", graph[2], " ", (end - start) * 1000)
    else:
        for graph in graphs:
            start_vertex = random.randint(0, graph[1]-1)


            start = time.perf_counter()
            result = bellman_ford.bellman_ford_matrix(graph[0], graph[1], start_vertex)
            end = time.perf_counter()

            if result == 1:
                outcomes.append(result)
            else:
                outcomes.append(0)

            times.append((end - start) * 1000)
            if (len(times) == repetitions):
                to_write.append({"vertexes": graph[1],"density": graph[2] ,"time": average(times), "probability": probability, "result": sum(outcomes)/len(outcomes)*100})
                times = []

            #print(graph[1], " ", graph[2], " ", (end - start) * 1000)


    with open(file_path, mode="a", newline="") as file:
        fieldnames = ["vertexes", "density", "time", "probability", "result"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(to_write)

def get_weight(probability):
    if probability == 0:
        return 1, 2
    elif probability == 1:
        return -2, -1
    else:
        min = -probability*100
        max = 99 - abs(min)
        return math.ceil(min), math.ceil(max)


def data_for_logistic_regression(type, num_vertexes, probability, repetitions, file_path):

    min, max = get_weight(probability)
    graphs = data_geneartor(type, num_vertexes, min, max, repetitions)

    get_time_prob(type, graphs, repetitions, probability, file_path)