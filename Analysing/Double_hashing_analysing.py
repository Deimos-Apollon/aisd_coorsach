from Analysing.AnalyseFunctions import analyse_insert_without_resize,\
    analyse_insert_with_resize, analyse_find, analyse_pop
from Hash_table_double_hashing.Hash_table_double_hashing import HashTableDoubleHashing
from random import randint


if __name__ == "__main__":
    ht = HashTableDoubleHashing()
    random_arr = [(randint(0, 1000000), i) for i in range(90000)]

    # checking insertion
    analyse_insert_without_resize(ht, random_arr, prefix="Double_hashing_figures")
    print(f"Checking insertion ht info", ht.get_table_info())

    # checking insertion with resize
    ht.clear()
    analyse_insert_with_resize(ht, random_arr, prefix="Double_hashing_figures")

    print(f"Checking insertion ht info", ht.get_table_info())
    # analyse find
    table_size_range = [8, 16, 32, 64, 128, 256, 512, 1024, 2048,
                        4096, 8192, 16384, 32768, 65536, 131072]
    ht_to_arr_dict = {HashTableDoubleHashing(j): [randint(0, i) for i in range(2*j)] for j in table_size_range}
    for index, ht_elem in enumerate(ht_to_arr_dict.keys()):
        ht_elem.hash_from_list_of_pairs((randint(0, 2*table_size_range[index]), i)
                                        for i in range(int(0.6 * table_size_range[index])))
        print(f"Checking #{index} finding ht info", ht_elem.get_table_info())
    analyse_find(ht_to_arr_dict, prefix="Double_hashing_figures")

    # analyse pop
    analyse_pop(ht_to_arr_dict, prefix="Double_hashing_figures")
