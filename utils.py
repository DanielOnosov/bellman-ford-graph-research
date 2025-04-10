import math


def checkConnectivity(n, p):
    c = (p * 100) / math.log1p(n)

    print(f"c = {c}")
    if c > 1:
        print("Almost always connected")
    else:
        print("Almost never connected")
