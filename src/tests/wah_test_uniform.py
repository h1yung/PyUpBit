import sys
sys.path.append("..")

import time
import numpy as np
import WAH

data = np.load("../../data/synthetic/uniform_d-100_n-100000000.npy")
data = np.array([1 if x == 1 else 0 for x in data])

start = time.time()
compressed = WAH.compress(data)
print("Compressed in %s" % time.strftime("%H:%M:%S", time.gmtime(time.time() - start)))

start = time.time()
decompressed = np.array(WAH.decompress(compressed))
print("Decompressed in %s" % time.strftime("%H:%M:%S", time.gmtime(time.time() - start)))

print()
print(np.all(data == decompressed))
