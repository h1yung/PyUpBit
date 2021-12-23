import os
import time
import sys ; sys.path.append("..")
import numpy as np

from upbit.upbit import UpBit
from ucb.ucb import UCB

def time_log(start_msg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(start_msg + "...")
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            print("Finished in %s\n" % time.strftime("%H:%M:%S:{}".format((elapsed%1000)), time.gmtime(elapsed/1000)))
            return result
        return wrapper
    return decorator


#distribution = "uniform"
distribution = "zipfian"
d, n = 100, int(1e5)
data_path = "../../data/synthetic/%s_d-%d_n-%d.npy" % (distribution, d, n)
print(data_path)
if not os.path.exists(data_path):
    print("Dataset (%s) does not exist.\nPlease run create_data.py to create synthetic dataset." % data_path)
    sys.exit()
data = np.load(data_path)
dataset = {"A": list(data)}

upbit = UpBit(dataset)
ucb = UCB(dataset)

@time_log("Inserting")
def test_insert(index):
    index.insert({"A": 1})
    if index == upbit:
        assert(len(upbit.bitmaps["A"].VB[1]) == len(upbit.bitmaps["A"].UB[1]) == n+1)
        assert(upbit.bitmaps["A"].VB[1][-1] == 1)
        assert(upbit.bitmaps["A"].VB[2][-1] == 0)

@time_log("Updating")
def test_update(index):
    rid = n
    index.update(rid, {"A": 2})
    if index == upbit:
        assert(len(upbit.bitmaps["A"].VB[1]) == len(upbit.bitmaps["A"].UB[1]) == n+1)
        assert(upbit.bitmaps["A"].UB[1][rid] == 1) # UB of old value flips
        assert(upbit.bitmaps["A"].UB[2][rid] == 1) # UB of new value flips
        assert(upbit.bitmaps["A"].UB[3][rid] == 0) # UB of other values are unchanged
        assert(upbit.bitmaps["A"].VB[1][rid] == 1) # VB of old value unchanged
        assert(upbit.bitmaps["A"].VB[2][rid] == 0) # VB of new value unchanged
        assert(upbit.bitmaps["A"].VB[3][rid] == 0) # VB of other values are unchanged

@time_log("Deleting")
def test_delete(index):
    rid = n
    index.delete(rid)
    if index == upbit:
        assert(len(upbit.bitmaps["A"].VB[1]) == len(upbit.bitmaps["A"].UB[1]) == n+1)
        assert(upbit.bitmaps["A"].UB[1][rid] == 1)
        assert(upbit.bitmaps["A"].UB[2][rid] == 0)
        assert(upbit.bitmaps["A"].VB[1][rid] == 1)
        assert(upbit.bitmaps["A"].VB[2][rid] == 0)

@time_log("Querying")
def test_query(index):
    query = index.query(("A", 1))
    assert(len(query) == len([x for x in data if x == 1]))
    assert(all(data[i] == 1 for i in query))

if __name__ == "__main__":
    print("Testing upbit...")
    test_insert(upbit)
    test_update(upbit)
    test_delete(upbit)
    test_query(upbit)

    print("\n\n\n")

    print("Testing UCB...")
    test_insert(ucb)
    test_update(ucb)
    test_delete(ucb)
    test_query(ucb)

