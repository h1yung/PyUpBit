import sys
import numpy as np
import matplotlib.pyplot as plt

data = np.load(sys.argv[1])

plt.hist(data, edgecolor='k')
plt.show()
