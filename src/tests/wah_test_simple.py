import sys
sys.path.append("..")

import time
import numpy as np
import WAH
from BitVector import BitVector

np.random.seed(1138)

d, n = 3, 62
data = np.random.randint(1, d, n)
data = [1 if x == 1 else 0 for x in data]
data += [0] * 10
data = np.array(data)
print("Data:")
for i in range(0, len(data), 31):
    idx = min(i+31, len(data))
    print(data[i:idx])

start = time.time()
compressed = WAH.compress(data)
print("Compressed:")
for i in range(0, len(compressed), 32):
    idx = min(i+32, len(compressed))
    print(compressed[i:idx])
print("Compressed in %s" % time.strftime("%H:%M:%S", time.gmtime(time.time() - start)))

print()
start = time.time()
decompressed = np.array(WAH.decompress(compressed))
print("Decompressed:")
for i in range(0, len(decompressed), 31):
    idx = min(i+31, len(decompressed))
    print(decompressed[i:idx])
print("Decompressed in %s" % time.strftime("%H:%M:%S", time.gmtime(time.time() - start)))

print()
print(np.all(data == decompressed))
