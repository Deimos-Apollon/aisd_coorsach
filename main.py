import time
from Hash_table_separate_chaining.Hash_table_sep_chain import *
from random import randint
import matplotlib.pyplot as plt

size = 10000
hs = HashTableSepChain(size)

arr = [(randint(0, 100000), 1) for i in range(6000)]
hs.hash_list_of_pairs(arr)

y = [len(i) for i in hs.__data__]
c = Counter()

for i in y:
    c[i] += 1

plt.plot(c.values())
plt.show()
