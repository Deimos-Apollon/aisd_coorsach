import time
from Hash_table_separate_chaining.Hash_table_sep_chain import *
from Hash_table_double_hashing.Hash_table_double_hashing import *

from random import randint
import matplotlib.pyplot as plt


map = []
arr = [randint(1, 1000) for _ in range(1000)]
times = Counter()
for index, i in enumerate(arr):
    start = time.process_time()
    map.append(i)
    total = time.process_time() - start
    times[index] = total
plt.plot(times.keys(), times.values())
plt.show()