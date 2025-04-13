import csv

import data_geneartor



def go():
    # probs = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
    #
    #
    # for i in range(20):
    #     data_for_logistic_regression("1", 50, probs[i], 30, "logistic4.csv")

    graphs = data_geneartor("1", 100, -1, 60, 30)
    data_geneartor.get_time("1", graphs, "lists_2001.csv")

    graphs = data_geneartor("2", 100, -1, 60, 30)
    data_geneartor.get_time("1", graphs, "matrixes_2001.csv")

    # input_file = "/Users/iv/PycharmProjects/Responses_Analyzer/matrixes_2001.csv"
    # output_file = "matrixes_2001.csv"
    # new_rows = []
    #
    # with open(input_file) as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         print(row)
    #         new_rows.append({"vertexes": row["vertexes"],
    #                          "edges": int(int(row["vertexes"]) * (int(row["vertexes"]) - 1) * float(row["density"])),
    #                          "density": row["density"], "time": row["time"]})
    #
    #     with open(output_file, mode="w", newline="") as file:
    #         fieldnames = ["vertexes", "edges", "density", "time"]
    #         writer = csv.DictWriter(file, fieldnames=fieldnames)
    #
    #         writer.writeheader()
    #         writer.writerows(new_rows)

go()