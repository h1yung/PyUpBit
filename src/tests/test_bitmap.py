import os
import sys ; sys.path.append("..")
import numpy as np

from upbit.bitmap import Bitmap

# For ease of testing, use small dataset with d=10 and n=1000
distribution = "uniform"
d, n = 10, 1000
data_path = "../../data/synthetic/%s_d-%d_n-%d.npy" % (distribution, d, n)
if not os.path.exists(data_path):
    print("Dataset (%s) does not exist.\nPlease run create_data.py to create synthetic dataset." % data_path)
    sys.exit()
data = np.load(data_path)

# Test bitmap for attribute = 1
bitmap = Bitmap(list(data))

# Should result in a bitmap with n+1 records, the last element being 1
bitmap.insert(6)
c = len(bitmap.VB[6])
d = len(bitmap.UB[6])
assert(c == d == n+1)
assert(bitmap.VB[6][-1] == 1)

# Should result in a bitmap with n+2 records, the last element being 1
bitmap.insert(1)
c = len(bitmap.VB[1])
d = len(bitmap.UB[1])
assert(c == d == n+2)
assert(bitmap.VB[1][-1] == 1)

# Should result in a bitmap with n+2 records, the first element being 0
bitmap.update(0, 1)
assert(len(bitmap.UB[1]) == len(bitmap.VB[1]) == n+2)
assert(bitmap.UB[1][0] == 1)
assert(bitmap.VB[1][0] == 0)

# Should result in a bitmap, still with n+2 records, with a negated value in update bitvector
# in this case, negation of 1 is 0
bitmap.delete(0)
assert(len(bitmap.UB[1]) == len(bitmap.VB[1]) == n+2)
assert(bitmap.UB[1][0] == 0)

print(bitmap.query(1))
