import time
from collections import Counter
import matplotlib.pyplot as plt
from Hash_table_separate_chaining.Hash_table_sep_chain import HashTableSepChain
from Hash_table_double_hashing.Hash_table_double_hashing import HashTableDoubleHashing
from random import randint


def compare_find(ht_sep_chain_list: [HashTableSepChain], ht_double_hash_list: [HashTableDoubleHashing],
                 arr_list: [[]]):
    times_number_for_table_size = Counter()
    all_times_for_table_size = Counter()
    best_times = Counter()
    worst_times = Counter()

    if len(ht_sep_chain_list) != len(ht_double_hash_list):
        raise ValueError('compare_find list lens is not equal')

    for ht_sep_chain, ht_double_hash, arr in zip(ht_sep_chain_list, ht_double_hash_list, arr_list):
        for elem_pair in arr:
            start = time.process_time()
            ht_sep_chain.find(elem_pair[0])
            total_time_ht_sep_chain = time.process_time() - start

            start = time.process_time()
            ht_double_hash.find(elem_pair[0])
            total_time_ht_double_hash = time.process_time() - start

            table_size = ht_double_hash.__size__
            if table_size != ht_sep_chain.__size__:
                raise ValueError('compare_find lens is not equal')

            total_time = (total_time_ht_double_hash / total_time_ht_sep_chain)
            all_times_for_table_size[table_size] += total_time
            times_number_for_table_size[table_size] += 1

        all_times_for_table_size[table_size] /= times_number_for_table_size[table_size]

    plt.figure()
    plt.title("График зависимости среднего времени для поиска элемента\n"
              " от размера таблицы")
    plt.xlabel("Размер таблицы")
    plt.ylabel("Среднее время для операции поиска, сек")
    plt.plot(all_times_for_table_size.keys(), all_times_for_table_size.values(), '--o')
    plt.savefig(f"Comparing_figures/find/mean_times.png", bbox_inches="tight")


def compare_insert(ht_sep_chain, ht_double_hash, arr):
    pass


def compare_pop(ht_sep_chain, ht_double_hash, arr):
    pass


if __name__ == "__main__":
    table_size_range = [8, 16, 32, 64, 128, 256, 512, 1024, 2048,
                        4096, 8192, 16384, 32768, 65536, 131072]
    ht_to_arr_dict_sep = {HashTableSepChain(j): [randint(0, i) for i in range(2 * j)] for j in table_size_range}
    for index, ht_elem in enumerate(ht_to_arr_dict_sep.keys()):
        ht_elem.hash_list_of_pairs((randint(0, 2 * table_size_range[index]), i)
                                   for i in range(int(0.6 * table_size_range[index])))
    ht_to_arr_dict_doub = {HashTableDoubleHashing(j): [randint(0, i) for i in range(2 * j)] for j in table_size_range}
    for index, ht_elem in enumerate(ht_to_arr_dict_doub.keys()):
        ht_elem.hash_from_list_of_pairs((randint(0, 2 * table_size_range[index]), i)
                                        for i in range(int(0.6 * table_size_range[index])))
    arr_list = []
    for table_size in table_size_range:
        arr_list.append([(randint(0, i), i) for i in range(2 * table_size)])

    compare_find(ht_to_arr_dict_sep.keys(), ht_to_arr_dict_doub.keys(), arr_list)
