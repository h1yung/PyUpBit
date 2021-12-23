import os
import numpy as np
import matplotlib.pyplot as plt

d, n = 100, int(1e5)
upbit = {
    "insert": 42.3316,
    "update": 3.5e-4,
    "delete": 2.4e-4,
    "search": 0.15515,
}

ucb = {
    "insert": 21.9832,
    "update": 23.2715,
    "delete": 9e-5,
    "search": 0.09014,
}
"""
upbit = {
    "insert": 249.26,
    "update": 0.0004,
    "delete": 0.0002,
    "search": 0.0927,
}

ucb = {
    "insert": 126.50,
    "update": 127.41,
    "delete": 1.76e-5,
    "search": 0.6111,
}
"""
if not os.path.exists("results"):
    os.mkdir("results")

labels = ["UCB", "UpBit"]
f, axarr = plt.subplots(2, 2, figsize=(10,10))
for (i, j), operation in zip([(0,0),(0,1),(1,0),(1,1)], upbit.keys()):
    axarr[i,j].bar(labels, [ucb[operation], upbit[operation]])
    axarr[i,j].set_title("%s, d=%d, n=%d" % (operation, d, n))
    axarr[i,j].set_ylabel("time (seconds)")
    plt.tight_layout()
plt.savefig("results/all.png")

