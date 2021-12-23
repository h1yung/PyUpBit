import os
import sys
import numpy as np
import scipy.stats as stats

SEED = 1138
UNIFORM = 0
ZIPFIAN = 1

np.random.seed(SEED)
datadir = "../data/synthetic"
if not os.path.isdir(datadir):
    os.mkdir(datadir)
# n: number of records
# d: cardinality of attribute domain
n = int(1e4)
d = 100
distribution = UNIFORM
if len(sys.argv) > 1 and sys.argv[1] == "-z":
    distribution = ZIPFIAN
if distribution == UNIFORM:
    data = np.random.randint(1, d+1, n)
    print("Saving")
    print(os.path.join(datadir, "uniform_d-%d_n-%d" % (d, n)))
    np.save(os.path.join(datadir, "uniform_d-%d_n-%d" % (d, n)), data)
elif distribution == ZIPFIAN:
    x = np.arange(1, d+1)
    a = 1.5
    weights = x ** (-a)
    weights /= weights.sum()
    bounded_zipf = stats.rv_discrete(name="bounded_zipf", values=(x, weights))
    data = bounded_zipf.rvs(size=n)
    np.save(os.path.join(datadir, "zipfian_d-%d_n-%d" % (d, n)), data)

