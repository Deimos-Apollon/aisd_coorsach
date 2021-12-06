import time
from collections import Counter

import matplotlib.pyplot as plt

from Analysing.Sep_chaining_figures.AnalyseFunctions import analyse_insert_without_resize,\
    analyse_insert_with_resize, analyse_find, analyse_pop
from Hash_table_separate_chaining.Hash_table_sep_chain import HashTableSepChain
from random import randint


if __name__ == "__main__":
    ht = HashTableSepChain()
    random_arr = [(randint(0, 100000), i) for i in range(100000)]

    # checking insertion
    analyse_insert_without_resize(ht, random_arr, prefix="Sep_chaining_figures")

    # checking insertion with resize
    ht.clear()
    analyse_insert_with_resize(ht, random_arr, prefix="Sep_chaining_figures")

    # analyse find
    table_size_range = [8, 16, 32, 64, 128, 256, 512, 1024, 2048,
                        4096, 8192, 16384, 32768, 65536]
    ht_to_arr_dict = {HashTableSepChain(j): [randint(0, i) for i in range(2*j)] for j in table_size_range}
    for index, ht_elem in enumerate(ht_to_arr_dict.keys()):
        ht_elem.hash_list_of_pairs((randint(0, 2*table_size_range[index]), i)
                                   for i in range(int(0.6 * table_size_range[index])))

    analyse_find(ht_to_arr_dict, prefix="Sep_chaining_figures")

    # analyse pop
    analyse_pop(ht_to_arr_dict, prefix="Sep_chaining_figures")
